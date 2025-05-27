// frappe.ui.form.on('Task', {
//   custom_customer_order_form: function(frm) {
//     if (frm.doc.custom_customer_order_form) {
//       frappe.call({
//         method: 'frappe.client.get',
//         args: {
//           doctype: 'Customer Order Form',
//           name: frm.doc.custom_customer_order_form
//         },
//         callback: function(r) {
//           if (r.message) {
//             const cof = r.message;

//             // Clear existing rows
//             frm.clear_table('custom_service_type');
//             frm.clear_table('custom_product_type');

//             // Copy Service Type Table
//             if (cof.service_type_table) {
//               cof.service_type_table.forEach(row => {
//                 let child = frm.add_child('custom_service_type');
//                 child.service_item = row.service_item;
//                 child.qty = row.qty;
//                 child.rate = row.rate;
//                 child.amount = row.amount;
//                 child.description = row.description;
//               });
//             }

//             // Copy Product Type Table
//             if (cof.product_type_table) {
//               cof.product_type_table.forEach(row => {
//                 let child = frm.add_child('custom_product_type');
//                 child.product_item = row.product_item;
//                 child.qty = row.qty;
//                 child.rate = row.rate;
//                 child.amount = row.amount;
//                 child.description = row.description;
//                 child.warranty = row.warranty;
//               });
//             }

//             frm.refresh_field('custom_service_type');
//             frm.refresh_field('custom_product_type');
//           }
//         }
//       });
//     }
//   }
// });


// frappe.ui.form.on('Task', {
//     refresh: function(frm) {
// 			console.log("Task form refreshed");
//         if(frm.doc.status === "Completed" && frm.doc.custom_sales_order) {
//             frm.add_custom_button("Update Sales Order Items", function() {
//                 frappe.call({
//                     method: "car_repair_management.car_repair_management.customization.task.task.update_sales_order_items_from_task",
//                     args: {
//                         task_name: frm.doc.name
//                     },
//                     callback: function(r) {
//                         if(!r.exc) {
//                             frappe.msgprint(r.message);
//                             frm.reload_doc();
//                         }
//                     }
//                 });
//             });
//         }
//     }
// });

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
