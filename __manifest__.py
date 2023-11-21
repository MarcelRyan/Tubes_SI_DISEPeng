# -*- coding: utf-8 -*-
{
    'name': "disepeng",
    'sequence': -100,
    'author': "Kelompok muSIngin",
    'category': 'disepeng',
    'description': """Module Odoo untuk perusahaan BPOM Makassar""",
    'version': '1.0',
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
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