# import frappe
# def post_check_list_fatch(doc, method=None):
# 	if doc.project:
# 		project = frappe.get_doc("Project", doc.project)
		
# 		if project.status == "Completed" and project.sales_order:
# 			sales_order = frappe.get_doc("Sales Order", project.sales_order)
			
# 			if sales_order.custom_customer_order_form:
# 				customer_order = frappe.get_doc("Customer Order Form", sales_order.custom_customer_order_form)
				
# 				doc.custom_customer_order_form = customer_order.name 

# 				doc.custom_post_check_list = 1
# 				doc.custom_vehicle_condition_summary = customer_order.vehicle_condition_summary
# 				doc.custom_odometer_reading = customer_order.odometer_reading
# 				doc.custom_engine_status = customer_order.engine_status
# 				doc.custom_oil_level = customer_order.oil_level
# 				doc.custom_body_damage = customer_order.body_damage
# 				doc.custom_tyre_condition = customer_order.tyre_condition
# 				doc.custom_battery_status = customer_order.battery_status

import frappe

def post_check_list_fatch(doc, method=None):
	if not doc.project:
		return
	project = frappe.get_doc("Project", doc.project)
	
	if project.status == "Completed" and project.sales_order:
		sales_order = frappe.get_doc("Sales Order", project.sales_order)

		if sales_order.custom_customer_order_form:
			customer_order = frappe.get_doc("Customer Order Form", sales_order.custom_customer_order_form)

			doc.custom_customer_order_form = customer_order.name
			doc.custom_post_check_list = 1
			doc.custom_vehicle_condition_summary = customer_order.vehicle_condition_summary
			doc.custom_odometer_reading = customer_order.odometer_reading
			doc.custom_engine_status = customer_order.engine_status
			doc.custom_oil_level = customer_order.oil_level
			doc.custom_body_damage = customer_order.body_damage
			doc.custom_tyre_condition = customer_order.tyre_condition
			doc.custom_battery_status = customer_order.battery_status
