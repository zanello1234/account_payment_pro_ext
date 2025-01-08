{
    'name': 'Account Payment USD Rate',
    'version': '17.0.1.0.0',
    'category': 'Accounting/Payment',
    'sequence': 14,
    'summary': 'Add manual USD rate for payments',
    'description': '''
Account Payment USD Rate
=======================
This module adds the ability to set a manual USD exchange rate for payments.
    ''',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'account_payment_pro',
    ],
    'data': [
        'views/account_payment_views.xml',
    ],
    'demo': [
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
