app_name = "car_repair_management"
app_title = "car_repair_management"
app_publisher = "Dhruvi Soliya"
app_description = "car_repair_management"
app_email = "dhruvi@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "car_repair_management",
# 		"logo": "/assets/car_repair_management/logo.png",
# 		"title": "car_repair_management",
# 		"route": "/car_repair_management",
# 		"has_permission": "car_repair_management.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/car_repair_management/css/car_repair_management.css"
# app_include_js = "/assets/car_repair_management/js/car_appointment_calendar.js"

# include js, css files in header of web template
# web_include_css = "/assets/car_repair_management/css/car_repair_management.css"
# web_include_js = "/assets/car_repair_management/js/car_repair_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "car_repair_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Job Card" : "car_repair_management/customization/job_card.js",
			  "Sales Order":"car_repair_management/customization/sales_order/sales_order.js",
			  "Task":"car_repair_management/customization/task/task.js",
			  "Customer":"car_repair_management/customization/customer/customer.js" }
			  
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "car_repair_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "car_repair_management.utils.jinja_methods",
# 	"filters": "car_repair_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "car_repair_management.install.before_install"
# after_install = "car_repair_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "car_repair_management.uninstall.before_uninstall"
# after_uninstall = "car_repair_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "car_repair_management.utils.before_app_install"
# after_app_install = "car_repair_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "car_repair_management.utils.before_app_uninstall"
# after_app_uninstall = "car_repair_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "car_repair_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		# "before_save": "car_repair_management.car_repair_management.customization.sales_order.sales_order.before_save",
		"on_submit": "car_repair_management.car_repair_management.customization.sales_order.sales_order.sales_order_on_submit"
	},
	"Task": {
		"on_update": "car_repair_management.car_repair_management.customization.task.task.on_task_update"
	},
	"Sales Invoice":{
		"before_save":"car_repair_management.car_repair_management.customization.sales_invoice.sales_invoice.post_check_list_fatch",
        "on_submit":"car_repair_management.car_repair_management.customization.sales_invoice.sales_invoice.fatch_serviceamount"
	}
	# "Customer Order Form": {
	# 	"on_save": "car_repair_management.customization.customer_order_form.customer_order_form.update_customer_service_info"
	# }
	
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"car_repair_management.tasks.all"
# 	],
# 	"daily": [
# 		"car_repair_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"car_repair_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"car_repair_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"car_repair_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "car_repair_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#     "erpnext.selling.doctype.sales_order.sales_order.update_items": "car_repair_management.car_repair_management.customization.task.task.custom_update_items"
# 	# "frappe.desk.doctype.event.event.get_events": "car_repair_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "car_repair_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["car_repair_management.utils.before_request"]
# after_request = ["car_repair_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["car_repair_management.utils.before_job"]
# after_job = ["car_repair_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"car_repair_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

