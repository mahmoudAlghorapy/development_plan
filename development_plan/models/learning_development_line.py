from odoo import models, fields, api


class LearningDevelopmentPlanLine(models.Model):
    _name = 'learning.development.line'

    development_line_id = fields.Many2one('development.plan')
    improve_area = fields.Text('Improvement Area(if any)')
    action = fields.Text('Action')

