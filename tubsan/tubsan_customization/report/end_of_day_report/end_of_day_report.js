// Copyright (c) 2023, Geoffrey Karani and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["End of Day Report"] = {
	"filters": [
		{
			fieldname: "sales_invoice",
			label: __("Sales Invoice"),
			fieldtype: "Link",
			options: "Sales Invoice",
			width: 100,
			reqd: 0
		},
		{
			fieldname: "customer",
			label: __("Customer"),
			fieldtype: "Link",
			options: "Customer",
			width: 10,
			reqd: 0,
		},
		{
			fieldname: "from",
			label: __("From Date"),
			fieldtype: "Date",
			width: 80,
			reqd: 1,
			default: dateutil.nowdate(),
		},
		{
			fieldname: "to",
			label: __("To Date"),
			fieldtype: "Date",
			width: 80,
			reqd: 1,
			default: dateutil.nowdate(),
		}
	]
};
