from odoo import models, fields, api

class SubscriptionPlan(models.Model):
    _name = 'smart.subscription.plan'
    _description = 'Subscription Plan'

    name = fields.Char(required=True, size= 45)
    price = fields.Float(required=True)
    duration = fields.Selection([
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ], required=True, default='yearly')
    description = fields.Text(size= 450)
    feature_ids = fields.One2many('smart.subscription.plan.feature', 'plan_id', string='Features')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This Name Is Exist!')
    ]

    @api.constrains('price')
    def _check_price_greater_50(self):
        for rec in self:
            if rec.price <= 50:
                raise ValidationError('Please Make Sure The Price Is Greater Than 50')


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