from odoo import models, fields

class DesignVersion(models.Model):
    _name = 'eng.design.version'
    _description = 'Design Version'

    name = fields.Char(string="Version Title", required=True)
    project_id = fields.Many2one('eng.engineering.project', string="Project", required=True)
    file_ids = fields.Many2many('ir.attachment', string="Design Files")
    date = fields.Date(string="Upload Date", default=fields.Date.today)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted to Client'),
        ('approved', 'Approved'),
        ('revision', 'Needs Revision')
    ], default='draft', string="Status")
    comment_ids = fields.One2many('eng.client.comment', 'version_id', string="Client Comments")

    def action_draft(self):
        for rec in self:
            rec.status = 'draft'

    def action_submitted(self):
        for rec in self:
            rec.status = 'submitted'

    def action_approved(self):
        for rec in self:
            rec.status = 'approved'

    def action_revision(self):
        for rec in self:
            rec.status = 'revision'
