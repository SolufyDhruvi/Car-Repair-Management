
frappe.ui.form.on('Sales Order', {
	refresh(frm) {
		frm.add_custom_button("Project Template", function(){
			frappe.set_route('Form', 'Project Template');
		},
		__("Create"))
	}
});

