from odoo import models, fields

class SubscriptionPlanFeature(models.Model):
    _name = 'smart.subscription.plan.feature'
    _description = 'Plan Feature'

    name = fields.Char(required=True)
    plan_id = fields.Many2one('smart.subscription.plan', required=True, ondelete='cascade')


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