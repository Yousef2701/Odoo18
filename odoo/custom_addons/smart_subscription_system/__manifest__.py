{
    'name': "Smart Subscription System",

    'summary': """Managing Recurring Subscription Plans""",

    'description': """
        A custom Odoo module for managing recurring subscription plans, customer enrollments, automated invoicing, and renewals
    """,

    'author': "Yousef Ibrahem Eissa",
    'category': '',
    'version': '18.0.0.1.0',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/subscription_plan_view.xml',
        'views/plan_feature_view.xml',
        'views/customer_subscription_view.xml'
    ],

    #'images': ['static/description/icon.png'],

    'demo': [
    
    ],

    'application': True
}