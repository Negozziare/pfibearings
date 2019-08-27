# -*- coding: utf-8 -*-


{
    'name': 'custom EDI for Mexico',
    'version': '1.1',
    'summary': 'Odoo Mexico Localization for Product and Partner',
    'sequence': 30,
    'description': """
    """,
    'category': 'COA of Mexico',
    'depends': ['l10n_mx_edi'],
    'data': [
        'views/edi_maxico_group.xml',
        'views/inherit_maxico_edi_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
}
