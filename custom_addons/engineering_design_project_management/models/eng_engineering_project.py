from odoo import models, fields, api

class EngineeringProject(models.Model):
    _name = 'eng.engineering.project'
    _description = 'Engineering Design Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Project Name", required=True)
    client_id = fields.Many2one('res.partner', string="Client", required=True)
    brief_id = fields.One2many('eng.design.brief', 'project_id', string="Design Brief")
    version_ids = fields.One2many('eng.design.version', 'project_id', string="Design Versions")
    task_ids = fields.One2many('eng.project.task', 'project_id', string="Project Tasks")
    file_ids = fields.One2many('eng.design.file', 'project_id', string="Project Files")
    feedback_ids = fields.One2many('eng.project.feedback', 'project_id', string="Feedback")
    stage = fields.Selection([
        ('new', 'New'),
        ('analysis', 'Requirements Analysis'),
        ('design', 'Design Phase'),
        ('review', 'Client Review'),
        ('revisions', 'Revisions'),
        ('approved', 'Approved'),
        ('delivered', 'Delivered'),
    ], default='new', string="Stage", tracking=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    description = fields.Text(string="Internal Notes")
