# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Library',
    'version' : '1.0',
    'summary': 'Library Management',
    'sequence': 10,
    'description': """
Library Management
====================
ce module permet de gerer le livres...etc
  """,
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menuitem.xml',
         'views/book_view.xml',
        'views/book_list_template.xml',
         ],
    'author':'hajer chelligue',
    'category': 'Services/Library',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}