# -*- coding: utf-8 -*-


{
    'name': 'custom EDI for Mexico',
    'version': '1.1',
    'summary': 'Odoo custom Mexico Localization for Product and Partner',
    'sequence': 30,
    'description': """
    """,
    'category': 'COA of Mexico',
    'depends': ['base_address_extended','l10n_mx_edi'],
    'data': [
        'views/inherit_res_partner_view.xml',
        'views/inherit_res_company_view.xml',
        'views/inherit_product_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
}
