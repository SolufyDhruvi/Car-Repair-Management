# Copyright (c) 2025, Dhruvi Soliya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class CustomerOrderForm(Document):
    # fatch data into customer doctype (service details)
	def on_update(self):
		if not self.customer_name:
			frappe.throw("Customer not selected in Customer Order Form.")
		customer = frappe.get_doc("Customer", self.customer_name)

		existing_plates = {row.license_plate for row in customer.custom_vehicle_service_info}

		for row in self.vehicle_detail:
			license_plate = row.license_plate
			if license_plate not in existing_plates:
				customer.append("custom_vehicle_service_info", {
					"license_plate": license_plate,
					"service_date": self.service_date,
					"serviced_by": self.mechanic_full_name
				})

		existing_template = {row.project_template for row in customer.custom_service_templates}

		if self.use_project_template == 1:
			if self.project_template not in existing_template:
				customer.append("custom_service_templates",{
					"project_template":self.project_template
				})
		else:
			existing_service = {row.item_name for row in customer.custom_service_taken_product_service}
			for s in self.service_type_table:
				item_name = s.service_name
				if item_name not in existing_service:
					customer.append("custom_service_taken_product_service",{
						"item_name":item_name,
						"quantity": s.qty
					})
			for p in self.product_type_table:
				product_name = p.product_name
				if item_name not in existing_service:
					customer.append("custom_service_taken_product_service",{
						"item_name":product_name
					})
		customer.save()
			
@frappe.whitelist()
def make_quotation_from_customer_order(source_name, target_doc=None):

	def post_process(source, target):
		for service in source.service_type_table:
			target.append("items", {
				"item_code": service.service_item,
				"item_name": service.service_name,
				"description": service.description or "",
				"qty": service.qty or 1,
				"uom": "Nos",
				"rate": service.rate or 0,
				"item_name": service.service_item,
			})

		for product in source.product_type_table:
			target.append("items", {
				"item_code": product.product_item,
				"item_name": product.product_name,
				"description": product.description or "",
				"qty": product.qty or 1,
				"uom": "Nos",
				"rate": product.rate or 0,
				"item_name": product.product_item,
			})

	return get_mapped_doc(
		"Customer Order Form",
		source_name,
		{
			"Customer Order Form": {
				"doctype": "Quotation",
				"field_map": {
					"customer_name": "party_name"
				}
			}
		},
		target_doc,
		post_process
	)

