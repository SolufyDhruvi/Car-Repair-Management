
frappe.ui.form.on('Sales Order', {
	refresh(frm) {
		frm.add_custom_button("Project Template", function(){
			frappe.set_route('Form', 'Project Template');
		},
		__("Create"))
	}
})

// frappe.ui.form.on("Sales Order", {
//     refresh: function (frm) {
//         if (frm.doc.docstatus === 1 && frm.doc.custom_project_template && !frm.doc.project) {
//             frm.add_custom_button("Project Template", function () {
//                 frappe.call({
//                     method: "car_repair_management.car_repair_management.customization.sales_order.sales_order.create_project_from_template_in_so",
//                     args: {
//                         sales_order_name: frm.doc.name,
//                         custom_project_template: frm.doc.custom_project_template
//                     },
//                     // callback: function (r) {
//                     //     if (r.message) {
//                     //         frappe.show_alert("Project Created: " + r.message);
//                     //         frm.reload_doc();
//                     //     }
//                     // }
//                 });
//             }, __("Create"));
//         }
//     }
// });
