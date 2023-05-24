from odoo import fields, models


class Produto(models.Model):
    _name = 'pedidos.produto'
    _description = 'Produto'
    _rec_name = 'nome'

    nome = fields.Char('Nome do Produto', required=True)
    descricao = fields.Text('Descrição do Pedido')
    preco = fields.Float('Preço do Produto')
    pedido_id = fields.Many2one('pedidos.pedido', 'Pedido')
