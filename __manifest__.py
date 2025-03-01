# -*- coding: utf-8 -*-
{
    'name': "role_based_views",

    'summary': "Sample module to display fields/views by role",

    'description': """
    This module extends the res.partner model by adding two fields:
    - field_for_role_1
    - field_for_role_2

    Two groups (Role 1 and Role 2) are defined and inherited views are created for each role.
    """,

    'author': "Dayron Peeta",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'security/rol_security.xml',
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

