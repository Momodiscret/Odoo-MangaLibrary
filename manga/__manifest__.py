# -*- coding: utf-8 -*-
{
    'name': "manga",

    'summary': "visionnage de mange",

    'description': """
gestion des manga
    """,

    'author': "Ibrahim",
    'website': "https://www.yourcompany.com",
    'application': True,

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/manga_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

