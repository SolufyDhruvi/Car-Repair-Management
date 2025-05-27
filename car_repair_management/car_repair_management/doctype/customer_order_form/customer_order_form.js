// Copyright (c) 2025, Dhruvi Soliya and contributors
// For license information, please see license.txt



frappe.ui.form.on('Customer Order Form', {
    refresh(frm) {
        frm.add_custom_button("Quotation", function () {
            frappe.call({
                method: 'car_repair_management.car_repair_management.doctype.customer_order_form.customer_order_form.make_quotation_from_customer_order',
                args: {
                    source_name: frm.doc.name
                },
                callback: function (r) {
                    if (r.message) {
                        frappe.model.sync(r.message);
                        frappe.set_route("Form", r.message.doctype, r.message.name);
                    }
                }
            });
        });
    }
});

//filter --> product type table and service type table and mechanic name(service manager)
frappe.ui.form.on('Customer Order Form', {
    onload: function(frm) {
        frm.set_query('mechanic_name', function() {
            return {
                filters: {
                    custom_is_service_manager: 1 
                }
            };
        });
        frm.fields_dict['service_type_table'].grid.get_field('service_item').get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    'is_stock_item': 0
                }
            };
        };
        frm.fields_dict['product_type_table'].grid.get_field('product_item').get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    'is_stock_item': 1
                }
            };
        };
    }
});

//item pricelist mathi rate fatch
frappe.ui.form.on('Service Type Table', {
    service_item: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];

        if (row.service_item) {
            frappe.call({
                method: "frappe.client.get_value",
                args: {
                    doctype: "Item Price",
                    filters: {
                        item_code: row.service_item,
                        selling: 1,
                        price_list: "Standard Selling" 
                    },
                    fieldname: ["price_list_rate"]
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.model.set_value(cdt, cdn, "rate", r.message.price_list_rate);

                        if (row.qty) {
                            frappe.model.set_value(cdt, cdn, "amount", row.qty * r.message.price_list_rate);
                        }
                    } else {
                        frappe.msgprint("No Item Price found for this Service Item.");
                    }
                }
            });
        }
    },

    qty: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.qty && row.rate) {
            frappe.model.set_value(cdt, cdn, "amount", row.qty * row.rate);
        }
    },

    rate: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.qty && row.rate) {
            frappe.model.set_value(cdt, cdn, "amount", row.qty * row.rate);
        }
    }
});

frappe.ui.form.on('Product Type Table', {
    product_item: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];

        if (row.product_item) {
            frappe.call({
                method: "frappe.client.get_value",
                args: {
                    doctype: "Item Price",
                    filters: {
                        item_code: row.product_item,
                        selling: 1,
                        price_list: "Standard Selling" 
                    },
                    fieldname: ["price_list_rate"]
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.model.set_value(cdt, cdn, "rate", r.message.price_list_rate);

                        if (row.qty) {
                            frappe.model.set_value(cdt, cdn, "amount", row.qty * r.message.price_list_rate);
                        }
                    } else {
                        frappe.msgprint("No Item Price found for this Product Item.");
                    }
                }
            });
        }
    },

    qty: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.qty && row.rate) {
            frappe.model.set_value(cdt, cdn, "amount", row.qty * row.rate);
        }
    },

    rate: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.qty && row.rate) {
            frappe.model.set_value(cdt, cdn, "amount", row.qty * row.rate);
        }
    }
});
