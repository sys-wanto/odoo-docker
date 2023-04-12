from odoo import models, fields, api

class Member(models.Model):
  _name         = 'online_store.member'
  _description  = "Tabel Member"


  member_nm = fields.Char('Nama')
  join_date = fields.Date('Tanggal Gabung')