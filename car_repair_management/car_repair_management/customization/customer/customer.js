frappe.ui.form.on('Customer', {
    refresh: function(frm) {
        frm.set_query("custom_serviced_by", function() {
            return {
                filters: {
                    custom_is_service_manager: 1
                }
            };
        });
    }
});
