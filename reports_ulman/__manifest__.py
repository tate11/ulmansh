# -*- coding: utf-8 -*-
{
    'name': "Ulman's Reports",

    'summary': """
    Customizaed Invoice Reports.
    """,

    'description': """

    """,

    'author': "Same Motion",
    'website': "http://www.samemotion.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Reports',
    'version': '1.0',
    'depends': ['account'],
    'data': [
        #'report/rep_layout_templates.xml',
        'report/report_templates.xml'  
    ],
    'demo': [
    ],
    'application': False,
}