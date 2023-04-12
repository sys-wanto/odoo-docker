from odoo import models, fields, api


class Barang(models.Model):
    _name = 'online_store.barang'
    _description = "Tabel Barang"

    nm_barang = fields.Char('nm_barang')
    category_id = fields.Many2one(
        comodel_name='online_store.category', string='category')
    stock = fields.Integer('stock')
    created_at = fields.Datetime('created_at')
    updated_at = fields.Datetime('updated_at')
