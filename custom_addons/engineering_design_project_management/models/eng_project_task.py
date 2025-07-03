from odoo import models, fields

class ProjectTask(models.Model):
    _name = 'eng.project.task'
    _description = 'Engineering Project Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Task Title", required=True)
    project_id = fields.Many2one('eng.engineering.project', string="Project", required=True)
    assigned_to = fields.Many2one('res.users', string="Assigned Engineer")
    deadline = fields.Date(string="Deadline")
    description = fields.Text(string="Description")
    state = fields.Selection([
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], default='todo', string="Status", tracking=True)
