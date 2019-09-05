# -*- coding: utf-8 -*-


{
    'name': 'custom EDI for Mexico',
    'version': '12.0',
    'summary': 'Odoo Mexico Localization for Product and Partner',
    'sequence': 30,
    'description': """
    """,
    'category': 'COA of Mexico',
    'depends': ['l10n_mx_edi'],
    'data': [
        'security/hide_field.xml',
        'views/edi_maxico_group.xml',
        'views/inherit_maxico_edi_view.xml',
        'views/res_compnay.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
}
