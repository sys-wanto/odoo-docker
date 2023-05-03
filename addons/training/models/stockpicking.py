from odoo import models, fields, api

class StockPicking(models.Model):
  _inherit  = 'stock.picking'

  driver = fields.Many2one(comodel_name='hr.employee', string='Driver')
  plat_number = fields.Char(string='Plat Number')
  # plat_number = fields.Many2one(comodel_name='ctu.cars', string='Plat Number')
  
  
  