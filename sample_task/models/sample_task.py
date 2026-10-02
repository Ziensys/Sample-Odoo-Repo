from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SampleTask(models.Model):
    _name = 'sample.task'
    _description = 'Sample Task'
    _order = 'priority desc, date_deadline, id'

    name = fields.Char(required=True)
    description = fields.Text()
    user_id = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user)
    date_deadline = fields.Date(string='Deadline')
    priority = fields.Selection(
        [('0', 'Normal'), ('1', 'High')],
        default='0',
    )
    state = fields.Selection(
        [('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')],
        default='todo',
        required=True,
    )
    estimated_hours = fields.Float()
    spent_hours = fields.Float()
    progress = fields.Float(compute='_compute_progress', store=True)
    active = fields.Boolean(default=True)

    @api.depends('estimated_hours', 'spent_hours')
    def _compute_progress(self):
        for task in self:
            if task.estimated_hours:
                task.progress = min(100.0, task.spent_hours / task.estimated_hours * 100.0)
            else:
                task.progress = 0.0

    @api.constrains('estimated_hours', 'spent_hours')
    def _check_hours(self):
        for task in self:
            if task.estimated_hours < 0 or task.spent_hours < 0:
                raise ValidationError(self.env._("Hours cannot be negative."))

    def action_start(self):
        self.write({'state': 'in_progress'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_reset(self):
        self.write({'state': 'todo'})
