from odoo import models, fields

class ClientComment(models.Model):
    _name = 'eng.client.comment'
    _description = 'Client Comment on Design Version'

    version_id = fields.Many2one('eng.design.version', string="Design Version", required=True)
    partner_id = fields.Many2one('res.partner', string="Client", required=True)
    comment = fields.Text(string="Comment", required=True)
    date = fields.Datetime(string="Date", default=fields.Datetime.now)
