# Copyright (c) 2025, Dhruvi Soliya and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

import frappe

def execute(filters=None):
	filters = filters or {}
	conditions = []

	if filters.get("from_date"):
		conditions.append(["service_date", ">=", filters["from_date"]])
	if filters.get("to_date"):
		conditions.append(["service_date", "<=", filters["to_date"]])
	if filters.get("mechanic_name"):
		conditions.append(["mechanic_name", "=", filters["mechanic_name"]])
	if filters.get("customer_name"):
		conditions.append(["customer_name", "=", filters["customer_name"]])

	columns = [
		{"label": "Order ID", "fieldname": "name", "fieldtype": "Link", "options": "Customer Order Form", "width": 150},
		{"label": "Order Date", "fieldname": "service_date", "fieldtype": "Date", "width": 120},
		{"label": "Mechanic", "fieldname": "mechanic_name", "fieldtype": "Link", "options": "Employee", "width": 150},
		{"label": "Mechanic Full Name", "fieldname": "mechanic_full_name", "fieldtype": "Data", "width": 180},
		{"label": "Customer", "fieldname": "customer_name", "fieldtype": "Link", "options": "Customer", "width": 150},
		{"label": "License Plates", "fieldname": "license_plates", "fieldtype": "Data", "width": 300},
		{"label": "Mobile Number", "fieldname": "mobile_number", "fieldtype": "Data", "width": 120},
		{"label": "Email", "fieldname": "email_address", "fieldtype": "Data", "width": 180},
	]

	data = []

	orders = frappe.get_all(
		"Customer Order Form",
		filters=conditions,
		fields=[
			"name", "service_date", "mechanic_name", "mechanic_full_name", 
			"customer_name", "mobile_number", "email_address"
		]
	)

	for order in orders:
		plates = frappe.get_all("Vehicle Detail", filters={"parent": order.name}, pluck="license_plate")
		plate_list = ", ".join(plates)

		data.append({
			"name": order.name,
			"service_date": order.service_date,
			"mechanic_name": order.mechanic_name,
			"mechanic_full_name": order.mechanic_full_name,
			"customer_name": order.customer_name,
			"license_plates": plate_list,
			"mobile_number": order.mobile_number,
			"email_address": order.email_address
		})

	return columns, data
