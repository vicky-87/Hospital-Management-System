# -*- coding: utf-8 -*-
{
    'name': "Hospital Management System",

    'summary': """
        Membuat Module OM Hospital""",

    'description': """
        Hospital Management
    """,

    'author': "Cendana2000",
    'category': 'Themes/front',
    'website': "https://www.cendana2000.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu_hospital.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'aplication':True
}
