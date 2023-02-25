# -*- coding: utf-8 -*-
{
    'name': "Development plan",

    'summary': """
        Development plan """,

    'description': """
        Development plan
    """,
    'author': "My Company",
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_appraisal'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/development_plan.xml',

    ],
}
