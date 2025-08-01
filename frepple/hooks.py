# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frepple"
app_title = "Frepple"
app_publisher = "Drayang Chua"
app_description = "Integration between ERPNext and Frepple"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "dchu0011@student.monash.edu"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frepple/css/frepple.css"
# app_include_js = "/assets/frepple/js/frepple.js"

# include js, css files in header of web template
# web_include_css = "/assets/frepple/css/frepple.css"
# web_include_js = "/assets/frepple/js/frepple.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frepple.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frepple.install.before_install"
# after_install = "frepple.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frepple.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doctype_js = {
    'Work Order':'public/js/work_order.js',
    'Purchase Order':'public/js/purchase_order.js',
    'Sales Order':'public/js/sales_order.js',
    'Bin':'public/js/bin.js',
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frepple.tasks.all"
# 	],
# 	"daily": [
# 		"frepple.tasks.daily"
# 	],
# 	"hourly": [
# 		"frepple.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frepple.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frepple.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frepple.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frepple.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frepple.task.get_dashboard_data"
# }


fixtures = [
    {"doctype": "Workspace", "filters": {"name": "Frepple"}},
]
