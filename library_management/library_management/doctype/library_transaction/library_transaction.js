// Copyright (c) 2020, ME and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Transaction', {
	"library_member": function(frm) {
		frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Library Member",
                name: frm.doc.library_member
            },
            callback: function (data) {
                console.log("get",data);
                frappe.model.set_value(frm.doctype,
                    frm.docname, "member_name",
                    data.message.first_name
                    + (data.message.member_last_name ?
                        (" " + data.message.member_last_name) : ""))
            }
        })

    },
    "article": function(frm) {
		frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Library Artical",
                name: frm.doc.article
            },
            callback: function (data) {
                console.log("get",data);
                frappe.model.set_value(frm.doctype,
                    frm.docname, "article_name",
                    data.message.article_name)
            }
        })

    }
});
