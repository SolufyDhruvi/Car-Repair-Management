import frappe
from frappe.model.document import Document
from frappe.utils import add_days, nowdate

#customer order form ma jetli pan item service table and product table ma hase ae task doctype ma pan dekhase 
def update_task_with_customer_order_items(task_name):
	task = frappe.get_doc("Task", task_name)

	if not task.custom_customer_order_form:
		return

	customer_order_name = task.custom_customer_order_form

	service_items = frappe.get_all("Service Type Table", {"parent": customer_order_name},["qty", "rate", "service_item", "amount"])
	product_items = frappe.get_all("Product Type Table", {"parent": customer_order_name},["qty", "rate", "product_item", "amount", "warranty"])

	task.set("custom_service_type", [])
	task.set("custom_product_type", [])

	for item in service_items:
		task.append("custom_service_type", {
			"qty": item.qty,
			"rate": item.rate,
			"service_item": item.service_item,
			"amount": item.amount
		})

	for item in product_items:
		task.append("custom_product_type", {
			"qty": item.qty,
			"rate": item.rate,
			"product_item": item.product_item,
			"amount": item.amount,
			"warranty": item.warranty
		})

	task.save()


def create_project_from_template_on_sales_order(doc, method=None):
	if doc.project:
		return doc.project

	customer_order_form = doc.custom_customer_order_form
	if not customer_order_form:
		frappe.throw("Customer Order Form is required to create project/tasks")

	# Use directly from Sales Order field
	project_template = doc.custom_project_template
	use_template = True if project_template else False

	project = frappe.new_doc("Project")
	project.project_name = f"{doc.name} - {doc.customer}"
	project.customer = doc.customer
	project.sales_order = doc.name
	project.status = "Open"

	if use_template:
		# Use project template to create project and tasks
		project.project_template = project_template
		project.save()

		doc.db_set("project", project.name)

		tasks = frappe.get_all("Task", filters={"project": project.name}, fields=["name"])

		for task in tasks:
			frappe.db.set_value("Task", task.name, {
				"custom_sales_order": doc.name,
				"custom_customer_order_form": customer_order_form
			})
			update_task_with_customer_order_items(task.name)

	else:
		# No template, create tasks dynamically from service/product tables
		project.save()
		doc.db_set("project", project.name)

		# Fetch service and product items from Customer Order Form
		service_items = frappe.get_all("Service Type Table", {"parent": customer_order_form},["qty", "rate", "service_item", "amount"])
		product_items = frappe.get_all("Product Type Table", {"parent": customer_order_form},["qty", "rate", "product_item", "amount", "warranty"])

		# Create one task per service item
		for s_item in service_items:
			item_name = frappe.db.get_value("Item", s_item.service_item, "item_name")

			task = frappe.new_doc("Task")
			task.subject = item_name or s_item.service_item
			task.project = project.name
			task.custom_sales_order = doc.name
			task.custom_customer_order_form = customer_order_form

			task.append("custom_service_type", {
				"qty": s_item.qty,
				"rate": s_item.rate,
				"service_item": s_item.service_item,
				"amount": s_item.amount
			})
			task.save()

		# Create one task per product item
		for p_item in product_items:
			item_name = frappe.db.get_value("Item", p_item.product_item, "item_name")

			task = frappe.new_doc("Task")
			task.subject = item_name or p_item.product_item
			task.project = project.name
			task.custom_sales_order = doc.name
			task.custom_customer_order_form = customer_order_form

			task.append("custom_product_type", {
				"qty": p_item.qty,
				"rate": p_item.rate,
				"product_item": p_item.product_item,
				"amount": p_item.amount,
				"warranty": p_item.warranty
			})
			task.save()

	return project.name


def sales_order_on_submit(doc, method=None):
	create_project_from_template_on_sales_order(doc, method=None)
	on_sales_order_submit(doc, method=None)

def on_sales_order_submit(doc, method=None):
	doc.db_set("status", "Open")

	
#fatch customer order form id quotation to sales order
# and from Sales Order to Sales Invoice
def before_save(doc, method=None):
	if doc.doctype == "Sales Order" and doc.quotation and not doc.custom_customer_order_form:
		quotation = frappe.get_doc("Quotation", doc.quotation)
		if quotation.custom_customer_order_form:
			doc.custom_customer_order_form = quotation.custom_customer_order_form

	if doc.doctype == "Sales Invoice" and doc.sales_order and not doc.custom_customer_order_form:
		sales_order = frappe.get_doc("Sales Order", doc.sales_order)
		if sales_order.custom_customer_order_form:
			doc.custom_customer_order_form = sales_order.custom_customer_order_form
			   