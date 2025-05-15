frappe.ui.form.on('Job Card', {
    onload: function(frm) {
        frm.set_query("employee", function() {
            return {
                filters: {
                    custom_is_technician_: 1
                }
            };
        });
    }
});

