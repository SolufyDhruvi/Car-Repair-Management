# Copyright (c) 2025, Dhruvi Soliya and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.query_builder import DocType
from frappe.utils import getdate

def execute(filters=None):
	filters = filters or {}
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Appointment ID"),
			"fieldname": "name", 
			"fieldtype": "Link", 
			"options": "Car Appointment", 
			"width": 150
		},
		{
			"label": _("Customer"), 
			"fieldname": "customer", 
			"fieldtype": "Data", 
			"width": 150
		},
		{
			"label": _("Mobile Number"), 
			"fieldname": "mobile_number", 
			"fieldtype": "Data", 
			"width": 120
		},
		{
			"label": _("Email Address"), 
			"fieldname": "email_address", 
			"fieldtype": "Data", 
			"width": 150
		},
		{
			"label": _("License Plate"), 
			"fieldname": "license_plate", 
			"fieldtype": "Data", 
			"width": 120
		},
		{
			"label": _("Issue Description"), 
			"fieldname": "issue_description", 
			"fieldtype": "Small Text", 
			"width": 200
		},
		{
			"label": _("Appointment Date"), 
			"fieldname": "appointment_date", 
			"fieldtype": "Date", 
			"width": 120
		},
		{
			"label": _("Appointment Time"), 
			"fieldname": "appointment_time", 
			"fieldtype": "Time", 
			"width": 100
		},
		{
			"label": _("Status"), 
			"fieldname": "status", 
			"fieldtype": "Data", 
			"width": 100
		},
	]

def get_data(filters):
	ca = DocType("Car Appointment")

	query = (
		frappe.qb.from_(ca)
		.select(
			ca.name,
			ca.customer,
			ca.mobile_number,
			ca.email_address,
			ca.license_plate,
			ca.issue_description,
			ca.appointment_date,
			ca.appointment_time,
			ca.status,
		)
	)
	if filters.get("from_date") and filters.get("to_date"):
		from_date = getdate(filters.get("from_date"))
		to_date = getdate(filters.get("to_date"))
		query = query.where(ca.appointment_date.between(from_date, to_date))

	if filters.get("status"):
		query = query.where(ca.status == filters["status"])

	query = query.orderby(ca.appointment_date)

	data = query.run(as_dict=True)
	return data
