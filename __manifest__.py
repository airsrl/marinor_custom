# -*- encoding: utf-8 -*-
{
    'name': 'Marinor custom',
    'version': '14.0',
    'description': 'Customizzazioni Marinor',
    'author': 'SC',
    'license': 'OPL-1',
    'category': "Extra Tools",
    'depends': ['base',
                'contacts',
                'sale_commission'],
    'data': [
        'views/res_partner.xml',
        'views/account_move.xml',
        'views/account_move_report.xml',

    ],
    'installable': True,
    'images': ['static/description/icon.png']
}

