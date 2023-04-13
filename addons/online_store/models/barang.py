from odoo import models, fields, api


class Barang(models.Model):
    _name = 'online_store.barang'
    _description = "Tabel Barang"

    nm_barang = fields.Char('Nama Barang')
    category = fields.Many2one(
        comodel_name='online_store.category', string='Category')
    stock = fields.Integer('Stock')
    created_at = fields.Datetime('Created at')
    updated_at = fields.Datetime('Updated at')
