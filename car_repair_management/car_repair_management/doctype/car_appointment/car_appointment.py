# Copyright (c) 2025, Dhruvi Soliya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
class CarAppointment(Document):
	def validate(self):
		for row in self.vehicle_detail:
			if row.license_plate:
				existing_appointment = frappe.db.get_value("Vehicle Detail",{"license_plate": row.license_plate,"parenttype": "Car Appointment", "parent": ["!=", self.name] },"parent")
				if existing_appointment:
					frappe.throw("This vehicle is already registered under another customer. Please check the license plate.")

		if not self.status:
			self.status = "Scheduled"
		
	@frappe.whitelist()
	def create_customer_order_form(self):
		customer_order = frappe.new_doc('Customer Order Form')
		customer_order.customer_name = self.customer
		customer_order.service_date = self.appointment_date
		customer_order.vehicle_condition_summary = self.issue_description
		customer_order.email_address = self.email_address
		customer_order.mobile_number = self.mobile_number

		for row in self.vehicle_detail:
			customer_order.append("vehicle_detail", {
				"license_plate": row.license_plate
			})
			
		customer_order.save()
		return customer_order.name

