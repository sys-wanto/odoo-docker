from odoo import models, fields, api

class Cart(models.Model):
    _name         = 'online_store.chart'
    _description  = "Tabel Chart"

    member_id   = fields.Many2one(comodel_name='online_store.member', string='Member')
    qty = fields.Integer('Quantity')
    updated_at  = fields.Datetime('updated_at')
    created_at  = fields.Datetime('created_at')
    
