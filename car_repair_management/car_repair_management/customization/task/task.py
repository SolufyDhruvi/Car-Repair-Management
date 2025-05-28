import frappe

# @frappe.whitelist()
# def update_sales_order_items_from_task(task_name):
#     task = frappe.get_doc("Task", task_name)

#     if not task.custom_sales_order:
#         frappe.throw("No Sales Order linked to this Task.")

#     if task.status != "Completed":
#         frappe.throw("Task must be marked as 'Completed' to update the Sales Order.")

#     so = frappe.get_doc("Sales Order", task.custom_sales_order)

#     existing_item_codes = [item.item_code for item in so.items]
#     extra_items = []

#     for used_item in task.custom_task_item_used:
#         if used_item.item_code not in existing_item_codes:
#             warehouse = frappe.get_cached_value("Item", used_item.item_code, "default_warehouse")
#             extra_items.append({
#                 "item_code": used_item.item_code,
#                 "qty": used_item.qty,
#                 "rate": used_item.rate or 0,
#                 "warehouse": warehouse or (so.items[0].warehouse if so.items else None)
#             })

#     if not extra_items:
#         return "No extra items to add."

#     if so.docstatus == 1:
#         so.cancel()

#     for item in extra_items:
#         so.append("items", item)

#     so.save()
#     so.submit()
#     frappe.db.commit()

#     return f"{len(extra_items)} extra item(s) added to Sales Order {so.name}."



def on_task_update(doc, method=None):
	if doc.project:
		project = frappe.get_doc("Project", doc.project)
		all_tasks = frappe.get_all("Task",{"project": doc.project},["status"])

		total_tasks = len(all_tasks)
		completed_tasks = len([t for t in all_tasks if t["status"] == "Completed"])

		if completed_tasks == 0:
			return

		if project.sales_order:
			so = frappe.get_doc("Sales Order", project.sales_order)

			if completed_tasks == total_tasks:
				so.db_set("status", "Completed")
			else:
				so.db_set("status", "On Hold")
