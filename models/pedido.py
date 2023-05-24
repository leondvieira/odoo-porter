from odoo import fields, models


class Pedido(models.Model):
    _name = 'pedidos.pedido'
    _description = 'Pedido'
    _rec_name = 'cliente'

    OPCOES_STATUS = [
        ('open', "Aberto"),
        ('in_progress', "Em Processo"),
        ('done', "Concluído"),
        ('canceled', "Cancelado"),
    ]

    cliente = fields.Char('Nome do Cliente', required=True)
    data = fields.Date()
    status = fields.Selection(OPCOES_STATUS, string="Status do Pedido", required=True)
    produto_ids = fields.One2many('pedidos.produto', 'pedido_id', string="Produtos")

    def finalizar_pedido(self):
        self.write({'status': "done"})

    def cancelar_pedido(self):
        self.write({'status': "canceled"})

    def processar_pedido(self):
        self.write({'status': "in_progress"})

    def abrir_pedido(self):
        self.write({'status': "open"})
