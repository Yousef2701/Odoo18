from odoo import models, fields

class CustomerSubscription(models.Model):
    _name = 'smart.customer.subscription'
    _description = 'Customer Subscription'

    customer_id = fields.Many2one('res.partner', required=True)
    plan_id = fields.Many2one('smart.subscription.plan', required=True)
    start_date = fields.Date(required=True, default=fields.Date.today)
    end_date = fields.Date(required=True)
    state = fields.Selection([
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled')
    ], default='active')
    auto_renew = fields.Boolean(default=True)


    # override create method

    # @api.model_create_multi
    # def create(self, vals):
    #   res = super().create(self, vals)
    #   # My Logic
    #   return res


    # override read method

    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
    #     res = super()._search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None)
    #     # My Logic
    #     return res


    # override update method

    # def write(self, vals):
    #   res = super().write(self, vals)
    #   # My Logic
    #   return res


    # override delete method

    # def unlink(self):
    #   res = super().unlink(self)
    #   # My Logic
    #   return res
