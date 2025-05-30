import frappe

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
