from odoo import models, fields, api

class Cars(models.Model):
  _name = 'ctu.cars'
  _description = "Cars"

  car_name = fields.Char(string='Nama Mobil')
  