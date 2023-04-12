from odoo import models, fields, api
from datetime import datetime


class Member(models.Model):
    _name = 'online_store.member'
    _description = "Tabel Member"

    member_nm = fields.Char('Nama')
    join_date = fields.Datetime('Tanggal Gabung', default=datetime.today())
