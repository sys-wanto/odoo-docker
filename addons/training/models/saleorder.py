from odoo import models, fields, api

class SaleOrder(models.Model):
  _inherit = 'sale.order'


  penanggung_jawab = fields.Many2one(comodel_name='hr.employee', string='Penanggung Jawab')
  project_id = fields.Many2one(comodel_name='ctu.project', string='Project')
  
  
