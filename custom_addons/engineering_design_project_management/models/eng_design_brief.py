from odoo import models, fields

class DesignBrief(models.Model):
    _name = 'eng.design.brief'
    _description = 'Design Brief'

    name = fields.Char(string="Brief Title", required=True)
    project_id = fields.Many2one('eng.engineering.project', string="Project", required=True)
    client_id = fields.Many2one('res.partner', string="Client", required=True)
    project_type = fields.Selection([
        ('architectural', 'Architectural'),
        ('mechanical', 'Mechanical'),
        ('electrical', 'Electrical'),
        ('civil', 'Civil'),
    ], string="Project Type", required=True)
    area = fields.Float(string="Site Area (m²)")
    purpose = fields.Text(string="Project Purpose")
    constraints = fields.Text(string="Constraints")
    file_ids = fields.Many2many('ir.attachment', string="Reference Files")
    notes = fields.Text(string="Additional Notes")
