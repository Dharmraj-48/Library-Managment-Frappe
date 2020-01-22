# -*- coding: utf-8 -*-
# Copyright (c) 2020, ME and contributors
# For license information, please see license.txt

# from __future__ import unicode_literals
# # import frappe
# from frappe.model.document import Document

# class LibraryTransaction(Document):
# 	pass
 
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class LibraryTransaction(Document):
    def validate(self):
        last_transaction = frappe.get_list("Library Transaction",
            fields=["transcation_type", "transcation_date"],
            filters = {
                "article": self.article,
                "transcation_date": ("<=", self.transcation_date),
                "name": ("!=", self.name)
            })
        if self.transcation_type=="Issue":
            msg = _("Article {0} {1} has not been recorded as returned since {2}")
            if last_transaction and last_transaction[0].transcation_type=="Issue":
                frappe.throw(msg.format(self.article, self.article_name,
                    last_transaction[0].transcation_date))
        else:
            if not last_transaction or last_transaction[0].transcation_type!="Issue":
                frappe.throw(_("Cannot return article not issued"))