# -*- coding: utf-8 -*-
{
    'name': "DISEPeng Odoo",
    'sequence': -100,
    'author': "Kelompok muSIngin",
    'category': 'Uncategorized',
    'description': """Module Odoo untuk perusahaan BPOM Makassar""",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/disepeng_menus.xml',
        'views/disepeng_forms.xml',
        'views/disepeng_trees.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}