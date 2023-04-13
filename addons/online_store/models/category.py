from odoo import models, fields, api
from datetime import datetime


class Category(models.Model):
    _name = "online_store.category"
    _description = "Tabel Category"

    category_nm = fields.Char('Nama Category')
    updated_at = fields.Datetime('Updated At', default=datetime.today(),)
    created_at = fields.Datetime('Created At', default=datetime.today())
