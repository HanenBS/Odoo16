{
    "name": "Library Members",
    "description": "Manage members borrowing books.",
    "author": "Daniel Reis",
    "license": "AGPL-3",
    "depends": ["library", "mail"],
    "application": True,
    "data": [
        "security/library_security.xml",
        "views/book_view.xml",
        "views/member_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
    ],
    'installable': True,
}
