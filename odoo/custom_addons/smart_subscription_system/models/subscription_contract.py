from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class SubscriptionContract(models.Model):
    _name = 'subscription.contract'
    _description = 'Subscription Contract'

    name = fields.Char(string='Contract Reference', required=True, default='New')
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    plan_id = fields.Many2one('subscription.plan', string='Plan', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', compute='_compute_end_date', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    renewal_log_ids = fields.One2many(
        'subscription.renewal.log',
        'contract_id',
        string='Renewal Logs'
    )

    @api.depends('start_date', 'plan_id')
    def _compute_end_date(self):
        for rec in self:
            if rec.start_date and rec.plan_id:
                rec.end_date = rec.start_date + relativedelta(months=rec.plan_id.duration_months)

    def activate_contract(self):
        self.write({'state': 'active'})

    def cancel_contract(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_active(self):
        for rec in self:
            rec.state = 'active'

    def action_expired(self):
        for rec in self:
            rec.state = 'expired'

    def action_cancelled(self):
        for rec in self:
            rec.state = 'cancelled'
