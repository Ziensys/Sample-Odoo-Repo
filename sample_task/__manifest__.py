{
    'name': 'Sample Tasks',
    'version': '19.0.1.0.0',
    'summary': 'Minimal task tracker used to test Odoo.sh deployments',
    'category': 'Productivity',
    'author': 'Ziensys',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/sample_task_views.xml',
        'views/sample_task_menus.xml',
    ],
    'application': True,
    'installable': True,
}
