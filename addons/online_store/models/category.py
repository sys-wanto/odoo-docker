from odoo import models, fields, api

class Category(models.Model):
    _name         = "online_store.category"
    _description  = "Tabel Category"

    nm_category = fields.Char('nm_category')
    updated_at  = fields.Datetime('updated_at')
    created_at  = fields.Datetime('created_at')