// Copyright (c) 2025, Dhruvi Soliya and contributors
// For license information, please see license.txt


frappe.ui.form.on('Car Appointment', {
    refresh: function(frm) {
        if(frm.doc.status === 'Confirmed') {
            frm.add_custom_button('Customer Order Form', function() {
                frm.call({
                    method: "create_customer_order_form",
                    args: {
                        car_appointment_name: frm.doc.name
                    },
                    doc:frm.doc,
                    callback: function(r) {
                        if(r.message) {
                            frappe.set_route('Form', 'Customer Order Form', r.message);
                        }
                    }
                });
            });
        }
    }
});
