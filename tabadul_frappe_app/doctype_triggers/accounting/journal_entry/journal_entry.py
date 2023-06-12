from __future__ import unicode_literals
import frappe
from frappe import _
import html
from bs4 import BeautifulSoup


@frappe.whitelist()
def before_insert(doc, method=None):
    pass
@frappe.whitelist()
def after_insert(doc, method=None):
    pass
@frappe.whitelist()
def onload(doc, method=None):
    pass
@frappe.whitelist()
def before_validate(doc, method=None):
    pass
@frappe.whitelist()
def validate(doc, method=None):
    for d in doc.accounts:
        if d.user_remark:
            html_string = str(d.user_remark)
            soup = BeautifulSoup(html_string, 'html.parser')
            plain_text = soup.get_text()
            #frappe.throw(plain_text)
            all_descriptions = frappe.db.sql(
            """
            SELECT name
            from `tabDescription Dimensions` 
            where `tabDescription Dimensions`.name = '{escaped_string}' 
            """.format(escaped_string=plain_text), as_dict=1)
            #all_descriptions = frappe.db.get_list('Description Dimensions', filters={'name': escaped_string})
            if all_descriptions :
                for m in all_descriptions :
                    descriptions = m.name
                    d.description_dimensions = descriptions
            if not all_descriptions:
                new_doc = frappe.get_doc(dict(
                doctype='Description Dimensions',
                name=plain_text,
                description_dimensions=plain_text,
                ))
                new_doc.insert(ignore_permissions=True)
                d.description_dimensions = new_doc.name
@frappe.whitelist()
def on_submit(doc, method=None):
    pass
@frappe.whitelist()
def on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def before_save(doc, method=None):
    pass
@frappe.whitelist()
def before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def on_update(doc, method=None):
    pass
