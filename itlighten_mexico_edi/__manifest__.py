# -*- coding: utf-8 -*-


{
    'name': 'custom EDI for Mexico',
    'version': '1.1',
    'summary': 'Odoo custom Mexico Localization for Product and Partner',
    'sequence': 30,
    'description': """
    """,
    'category': 'COA of Mexico',
    'depends': ['l10n_mx_edi'],
    'data': [
        'views/inherit_res_partner_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
}
