from odoo import models, fields

class DesignFile(models.Model):
    _name = 'eng.design.file'
    _description = 'Design File'

    name = fields.Char(string="File Title", required=True)
    project_id = fields.Many2one('eng.engineering.project', string="Project", required=True)
    version_id = fields.Many2one('eng.design.version', string="Design Version", ondelete='set null')
    attachment_id = fields.Many2one('ir.attachment', string="File", required=True)
    uploaded_by = fields.Many2one('res.users', string="Uploaded By", default=lambda self: self.env.user)
    upload_date = fields.Datetime(string="Upload Date", default=fields.Datetime.now)
