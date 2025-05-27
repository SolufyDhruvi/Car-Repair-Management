// Copyright (c) 2025, Dhruvi Soliya and contributors
// For license information, please see license.txt

frappe.query_reports["Appointment Schedule"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": "From Date",
			"fieldtype": "Date",
			"default": frappe.datetime.add_days(frappe.datetime.get_today(), -7)
		},
		{
			"fieldname": "to_date",
			"label": "To Date",
			"fieldtype": "Date",
			"default": frappe.datetime.get_today()
		},
        {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "\nScheduled\nConfirmed"
        }
	]
};
