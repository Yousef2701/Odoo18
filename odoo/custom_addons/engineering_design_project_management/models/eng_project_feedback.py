from odoo import models, fields

class ProjectFeedback(models.Model):
    _name = 'eng.project.feedback'
    _description = 'Project Feedback'

    project_id = fields.Many2one('eng.engineering.project', string="Project", required=True)
    partner_id = fields.Many2one('res.partner', string="Client", required=True)
    rating = fields.Selection([
        ('1', 'Very Poor'),
        ('2', 'Poor'),
        ('3', 'Average'),
        ('4', 'Good'),
        ('5', 'Excellent'),
    ], string="Rating")
    comment = fields.Text(string="Feedback Comment")
    date = fields.Datetime(string="Submitted On", default=fields.Datetime.now)
