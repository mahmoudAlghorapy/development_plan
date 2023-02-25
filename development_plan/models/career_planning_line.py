from odoo import models, fields, api


class CareerPlanningLine(models.Model):
    _name = 'career.planning.line'

    planning_id = fields.Many2one('development.plan')
    short_term = fields.Text('Short term')
    long_term = fields.Text('Long term')

