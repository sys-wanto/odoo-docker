from odoo import models, fields, api


class RefPropinsi(models.Model):
    _name = 'ctu.ref_propinsi'
    _description = 'ctu.ref_propinsi'

    kd_propinsi = fields.Integer('kd_propinsi')
    nm_propinsi = fields.Char('nm_propinsi')
    created_at = fields.Datetime('created_at')
    updated_at = fields.Datetime('updated_at')
