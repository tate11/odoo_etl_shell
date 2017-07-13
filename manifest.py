# -*- coding: utf-8 -*-
{
    'name': "Odoo ETL Shell",

    'application': True,

    'summary': """
        A rudimentary framework that serves as a basis for creating complex Odoo ETL modules""",

    'description': """
        A rudimentary framework that serves as a basis for creating complex Odoo ETL modules
    """,

    'author': "community",
    'website': "https://github.com/idazco/odoo-etl-shell",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'views/data_mapping.xml',
        'views/res_config.xml',
    ],
    'qweb': [],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}