from odoo import models, fields, api


class Project(models.Model):
    _name = 'ctu.project'
    _description = "Project"

    name              = fields.Char('Name')
    customer          = fields.Many2one('res.partner', string='Customer')
    penanggung_jawab  = fields.Many2one('hr.employee', string='Penanggung Jawab')
    start_date        = fields.Date('Start Date')
    end_date          = fields.Date('End Date')
    budget            = fields.Integer('Budget')
    margin            = fields.Integer('Margin (%)')
    total             = fields.Float('Total')
