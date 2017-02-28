# -*- coding: utf-8 -*-
{
    'name': "Communities by Country Menu (UG, RW, BDI)",

    'summary': """
        Adds Uganda/Rwanda/Burundi menu items to the left menu under 'communities'""",

    'description': """
        Adds Uganda/Rwanda/Burundi menu items to the left menu under 'communities'
    """,

    'author': "Spark MicroGrnats",
    'website': "http://www.sparkmicrogrants.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sparkit'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
