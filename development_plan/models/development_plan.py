from odoo import models, fields, api


class DevelopmentPlan(models.Model):
    _name = 'development.plan'

    employee_name_id = fields.Many2one('hr.employee', string='Employee Name')
    employee_id = fields.Integer(related='employee_name_id.id',
                                 string='Employee ID')
    job_position_id = fields.Many2one('hr.job', related='employee_name_id.job_id',
                                      string='Job position')
    department_id = fields.Many2one('hr.department', related='employee_name_id.department_id',
                                    string='Department')
    planning_ids = fields.One2many('career.planning.line', 'planning_id', string='Career Planning')
    development_line_ids = fields.One2many('learning.development.line', 'development_line_id', string='Learning  Plan')
    comments_ids = fields.One2many('additional.comments.line', 'comments_id', string='Additional comments')
    training_line_ids = fields.One2many('training.development.line', 'training_line_id', string='Training Section')
    states = fields.Selection([('draft', 'Draft'),
                               ('confirm', 'Confirm')],
                              string='Status', tracking=True, default='draft',  clickable='1')
    color = fields.Integer()


    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'
