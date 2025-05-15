# import frappe


# @frappe.whitelist()
# def create_project_from_template_in_so(sales_order_name, custom_project_template):
#     sales_order = frappe.get_doc("Sales Order", sales_order_name)

#     if not custom_project_template:
#         frappe.throw("Project Template is required.")

#     project = frappe.new_doc("Project")
#     # project.project_name = f"{sales_order.name} - {sales_order.customer}"
#     project.custom_project_template = custom_project_template
#     project.customer = sales_order.customer
#     project.sales_order = sales_order.name
#     project.status = "Open"
#     project.save()

#     sales_order.db_set("project", project.name)

#     return project.name
