from odoo import models, fields, api

class CartDetail(models.Model):
    _name         = 'online_store.cart_detail'
    _description  = "Tabel Cart Detail"

    chart_id = fields.Many2one(comodel_name='online_store.cart', string='cart')
    barang_id = fields.Many2many(comodel_name='online_store.barang', string='barang')
    
    