from odoo import models, fields, api


class Cart(models.Model):
    _name = 'online_store.chart'
    _description = "Tabel Chart"

    customer = fields.Many2one(comodel_name='hr.employee', string='Customer')
    qty = fields.Integer('Quantity')
    updated_at = fields.Datetime('Updated At')
    created_at = fields.Datetime('Created At')
