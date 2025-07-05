from odoo import models, fields

class SubscriptionPlan(models.Model):
    _name = 'subscription.plan'
    _description = 'Subscription Plan'

    name = fields.Char(string='Plan Name', required=True)
    price = fields.Float(string='Price', required=True)
    duration_months = fields.Integer(string='Duration (Months)', required=True)
    
    feature_ids = fields.Many2many(
        'plan.feature', 
        string='Features'
    )

    contract_ids = fields.One2many(
        'subscription.contract', 
        'plan_id', 
        string='Contracts'
    )



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