from odoo import models, fields, api


class CartDetail(models.Model):
    _name = 'online_store.cart_detail'
    _description = "Tabel Cart Detail"

    chart = fields.Many2one(comodel_name='online_store.cart', string='Cart')
    barang = fields.Many2many(
        comodel_name='online_store.barang', string='Barang')
