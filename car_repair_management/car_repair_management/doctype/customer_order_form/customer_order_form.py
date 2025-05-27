# Copyright (c) 2025, Dhruvi Soliya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class CustomerOrderForm(Document):
	pass

@frappe.whitelist()
def make_quotation_from_customer_order(source_name, target_doc=None):

    def post_process(source, target):
        for service in source.service_type_table:
            target.append("items", {
                "item_code": service.service_item,
                "item_name": service.service_name,
                "description": service.description or "",
                "qty": service.qty or 1,
                "uom": "Nos",
                "rate": service.rate or 0,
                "item_name": service.service_item,
            })

        for product in source.product_type_table:
            target.append("items", {
                "item_code": product.product_item,
                "item_name": product.product_name,
                "description": product.description or "",
                "qty": product.qty or 1,
                "uom": "Nos",
                "rate": product.rate or 0,
                "item_name": product.product_item,
            })

    return get_mapped_doc(
        "Customer Order Form",
        source_name,
        {
            "Customer Order Form": {
                "doctype": "Quotation",
                "field_map": {
                    "customer_name": "party_name"
                }
            }
        },
        target_doc,
        post_process
    )
