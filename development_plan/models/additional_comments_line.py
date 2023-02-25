from odoo import models, fields, api


class AdditionalCommentsLine(models.Model):
    _name = 'additional.comments.line'

    comments_id = fields.Many2one('development.plan')
    employee = fields.Text('Employee')
    direct_manager = fields.Text('Direct Manager')

