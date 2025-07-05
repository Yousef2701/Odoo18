{
    'name': "Smart Subscription System",

    "summary": """Manage SaaS-style recurring subscriptions with plans, features, and renewals.""",

    "description": """
        Smart Subscription System
        =========================
        A complete subscription management system for SaaS models. 
        Includes:
        - Subscription plans with features
        - Recurring contracts
        - Automated renewals with logging
        - Integration with Odoo Accounting
        - Email notifications and analytics
    """,

    'author': "Yousef Ibrahem Eissa",
    "category": "Sales/Subscription",
    'version': '18.0.0.1.0',

    "depends": ["base", "mail", "account"],

    'data': [
        'security/ir.model.access.csv',
        'views/plan_feature_view.xml',
        'views/subscription_contract_view.xml',
        'views/subscription_plan_view.xml',
        'views/subscription_renewal_log_view.xml',
        'views/base_menu.xml'
    ],

    'demo': [
        'demo/demo_data.xml'
    ],

    'application': True
}