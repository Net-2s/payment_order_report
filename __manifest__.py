# -*- coding: utf-8 -*-
{
    'name': "Payment Order Report",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/ir_payment_order_sequence.xml',
        'views/sale_order.xml',
        'views/res_partner.xml',
        'reports/payment_order_report_template.xml',
        'reports/payment_order_report_view.xml',

    ],
}
