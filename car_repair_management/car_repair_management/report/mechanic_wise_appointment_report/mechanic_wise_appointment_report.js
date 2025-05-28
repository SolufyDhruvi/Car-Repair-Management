// Copyright (c) 2025, Dhruvi Soliya and contributors
// For license information, please see license.txt

frappe.query_reports["Mechanic-wise Appointment Report"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": "From Date",
			"fieldtype": "Date",
			"reqd": 1
		},
		{
			"fieldname": "to_date",
			"label": "To Date",
			"fieldtype": "Date",
			"reqd": 1
		},
		{
			"fieldname": "mechanic_name",
			"label": "Mechanic",
			"fieldtype": "Link",
			"options": "Employee"
		},
		{
			"fieldname": "customer_name",
			"label": "Customer",
			"fieldtype": "Link",
			"options": "Customer"
		}
	]
};

