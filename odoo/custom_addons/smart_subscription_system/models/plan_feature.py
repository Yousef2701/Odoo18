from odoo import models, fields

class PlanFeature(models.Model):
    _name = 'plan.feature'
    _description = 'Plan Feature'

    name = fields.Char(string='Feature Name', required=True)
    description = fields.Text(string='Description')

    plan_ids = fields.Many2many('subscription.plan', string='Plans')



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