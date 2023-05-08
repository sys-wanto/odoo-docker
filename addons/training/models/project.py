from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


class Project(models.Model):
    _name = 'ctu.project'
    _description = "Project"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char('Name')
    customer = fields.Many2one('res.partner', string='Customer')
    penanggung_jawab = fields.Many2one(
        'hr.employee', string='Penanggung Jawab')
    projects_quotation = fields.One2many(
        comodel_name='sale.order', inverse_name='project_id', string='Sales')

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
                    total += sub_project.budget * sub_project.qty
                    rec.budget = total

    @api.constrains('project_id')
    def create_sales_order(self):
        for rec in self:
            sales_order = self.env['sale.order'].create(
                {
                    'partner_id': rec.customer.id,
                    'project_id': rec.id
                }
            )
            if sales_order:
                if rec.sub_project_ids:
                    for sub_project in rec.sub_project_ids:
                        sales_order.order_line.create(
                            {
                                'order_id': sales_order.id,
                                'product_id': sub_project.name.id,
                                'product_uom_qty': sub_project.qty,
                            }
                        )

    def smart_button_link(self):
        for rec in self:
            return {
                'name': 'Quotation',
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'view_mode': 'tree',
                'domain': [('project_id', '=', rec.name)],
                'context': "{'create': False}"
            }

class SubProject(models.Model):
    _name = 'ctu.sub_project'
    _description = "Sub Project"

    project_id = fields.Many2one('ctu.project', string='project')
    # name = fields.Char('name')
    name = fields.Many2one(comodel_name='product.product', string='name', domain=[
                           ('detailed_type', '=', 'service')])
    qty = fields.Integer('qty')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    budget = fields.Float('budget', related='name.list_price')
