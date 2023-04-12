from odoo import models, fields, api

class Training(models.Model):
     _name = 'ctu.training'
     _description = 'ctu.training'

     name           = fields.Char("Nama")
     tanggal        = fields.Date("Tanggal")
     pengajar       = fields.Char("Pengajar")
     jumlah_peserta = fields.Integer("Jumlah Peserta")