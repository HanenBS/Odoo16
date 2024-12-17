{
    "name": "Library Book Checkout",
    "description": "Members can borrow books from the library.",
    "author": "Daniel Reis",
    "license": "AGPL-3",
    "depends": ["library_member", "mail", "contacts"],
    'installable': True,
    "data": [
        "security/ir.model.access.csv",
        "views/library_menu.xml",
        "views/checkout_view.xml",
        "views/checkout_kanban_view.xml",  # Ch11
        "views/assets.xml",  # Ch11, until Odoo 14
        "data/stage_data.xml",
    ],
    "assets": {  # Ch11, since Odoo 15
        "web.assets_backend": {
            "library_checkout/static/src/css/checkout.css",
            "library_checkout/static/src/js/checkout.js",
        }
    }
}
