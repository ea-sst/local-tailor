# -*- coding: utf-8 -*-
{
    'name': 'Advanced Sales Management (Clothing Business)',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage and customise measurements and designs in the sales process, with automatic data population and PDF invoice printing.',
    'description': """
    The Sale Management Extended module for Odoo enhances the sales order process for Businessses by allowing detailed input of product measurements and designs, automatically populating customer-specific default measurements, and generating measurement invoices in PDF format. It also ensures that any updates to measurements during the sales process are reflected in the customer's master data, maintaining accurate records for future orders.
""",
    'author': 'Supply Steer Technologies',
    'company': 'Supply Steer Technologies',
    'website': "https://www.supplysteer.com",
    'license': 'Other proprietary',

    'depends': ['contacts'],
    'data': [
        'data/ir_sequence.xml',
        'views/partner_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sales_clothing/static/src/css/tailor_rtl.css',
        ]
    },
    'installable': True,
    'application': True,
}
