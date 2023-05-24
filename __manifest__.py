{
    'name': 'Pedidos',
    'description': 'App de Pedidos CondoTech.',
    'author': 'Leonardo Vieira',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'security/pedido_security.xml',
        'views/pedido_menu.xml',
        'views/pedido_view.xml',
    ]
}