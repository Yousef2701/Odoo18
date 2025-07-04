{
    'name': "Engineering Design Project Management",

    'summary': """Manage engineering design projects with client portal, version control, and full project lifecycle tracking.""",

    "description": """
        Engineering Design Studio – Project Management Module

        This module is designed for companies specialized in engineering design services (architectural, mechanical, structural, etc.). It helps manage the full lifecycle of design projects from initial client request to final delivery.

        Main Features:
        - Client Portal to submit design requests and track project status
        - Structured design brief form capturing project requirements
        - Project lifecycle tracking with kanban stages
        - Internal task assignments and timesheet tracking
        - Design versioning and approval workflow
        - File management for each project and design version
        - Commenting system between clients and designers
        - Project dashboards and reporting for managers

        Ideal for firms that provide custom design services and want to streamline client communication, design feedback, and internal workflow.
    """,

    'author': "Yousef Ibrahem Eissa",
    'category': '',
    'version': '18.0.0.1.0',

    'depends': ['base', 'mail', 'project', 'contacts', 'web'],

    'data': [
       'security/ir.model.access.csv',
        'views/engineering_project_view.xml',
        'views/design_brief_view.xml',
        'views/design_version_view.xml',
        'views/project_task_view.xml',
        'views/design_file_view.xml',
        'views/client_comment_view.xml',
        'views/project_feedback_view.xml',
        'views/base_menu.xml'
    ],

    'demo': [
        'demo/demo_data.xml'
    ],

    'application': True
}