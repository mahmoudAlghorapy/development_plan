from datetime import datetime, date
from odoo import models, fields, api


class TrainingDevelopmentLine(models.Model):
    _name = 'training.development.line'

    training_line_id = fields.Many2one('development.plan')
    training_course = fields.Many2one('hr.employee', 'Training Course')
    institute_source = fields.Text('Institute or Source')
    preferred_date = fields.Datetime('Preferred Date', default=fields.Date.today)

