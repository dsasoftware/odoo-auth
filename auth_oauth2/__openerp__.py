
{
    'name': 'OAuth2 Authentication',
    'version': '1.0',
    'category': 'Anybox',
    'description': """
        Allow users to sign up through OAuth2 Provider.

        Please, visit https://github.com/anybox/auth_oauth2 to get more
        informations.
    """,
    'author': 'Anybox',
    'website': 'http://anybox.fr',
    'depends': ['base', 'web', 'share'],
    'external_dependencies': {
        'python': ['oauth2client'],
    },
    'data': [
        'data/res_users_view.xml',
        'static/src/xml/auth_oauth2.xml',
        'views/auth_oauth2_view.xml',
    ],
    'demo': [
        'demo/res_users.xml',
    ],
    'js': [
        'static/src/js/auth_oauth2.js'
    ],
    'css': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
