frappe.ui.form.on('Task', {
    refresh: function(frm) {
            frm.add_custom_button("Update SO Items", function () {
                frappe.call({
                    method: "car_repair_management.car_repair_management.customization.task.task.update_sales_order_items_from_task",
                    args: {
                        task_name: frm.doc.name
                    },
                    callback: function (r) {
                        if (!r.exc) {
                            frappe.msgprint(r.message);
                        }
                    }
                });
            });
        
    }
});
