from odoo import models, fields, api
from datetime import datetime


class Category(models.Model):
    _name = "online_store.category"
    _description = "Tabel Category"

    category_nm = fields.Char('category_nm')
    updated_at = fields.Datetime('updated_at', default=datetime.today(),)
    created_at = fields.Datetime('created_at', default=datetime.today())
