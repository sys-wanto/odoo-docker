from odoo import models, fields, api


class Project(models.Model):
    _name = 'ctu.project'
    _description = "Project"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char('Name')
    customer = fields.Many2one('res.partner', string='Customer')
    penanggung_jawab = fields.Many2one(
        'hr.employee', string='Penanggung Jawab')
    start_date = fields.Date('Start Date', tracking=True)
    end_date = fields.Date('End Date')
    budget = fields.Integer(
        'Budget', compute="_compute_budget", readonly=True, store=True)
    margin = fields.Integer('Margin (%)')
    total = fields.Float('Total')

    sub_project_ids = fields.One2many(
        'ctu.sub_project', 'project_id', string='Sub Project')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
    ], string='State', default="draft")

    def set_to_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def set_to_draft(self):
        for rec in self:
            rec.state = 'draft'

    def set_to_done(self):
        for rec in self:
            rec.state = 'done'

    @api.depends('sub_project_ids.budget')
    def _compute_budget(self):
        for rec in self:
            if rec.sub_project_ids:
                total = 0
                for sub_project in rec.sub_project_ids:
                    total += sub_project.budget
                rec.budget = total

class SubProject(models.Model):
    _name = 'ctu.sub_project'
    _description = "Sub Project"

    project_id = fields.Many2one('ctu.project', string='project')
    name = fields.Char('name')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    budget = fields.Integer('budget')
