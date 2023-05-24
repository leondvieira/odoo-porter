from odoo import fields, models


class Pedido(models.Model):

    OPCOES_STATUS = [
        ('open', "Aberto"),
        ('in_progress', "Em Processo"),
        ('done', "Concluído"),
        ('canceled', "Cancelado"),
    ]

    _name = 'pedidos.pedido'
    _description = 'Pedido'
    cliente = fields.Char('Nome do Cliente', required=True)
    data = fields.Date()
    status = fields.Selection(OPCOES_STATUS, string="Status do Pedido")
    produto_ids = fields.One2many('pedidos.produto', 'pedido_id', string="Produtos")
