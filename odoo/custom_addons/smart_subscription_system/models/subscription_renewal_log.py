from odoo import models, fields

class SubscriptionRenewalLog(models.Model):
    _name = 'subscription.renewal.log'
    _description = 'Subscription Renewal Log'

    contract_id = fields.Many2one(
        'subscription.contract', 
        string='Contract', 
        required=True,
        ondelete='cascade'
    )
    renewal_date = fields.Date(string='Renewal Date', required=True)
    status = fields.Selection([
        ('success', 'Success'),
        ('failed', 'Failed')
    ], string='Status', required=True)
    note = fields.Text(string='Notes')
