from odoo import models, fields, api

class CarType(models.Model):
    _name = 'workshop_bjm.car_type'
    _description = 'Car Types'

    name = fields.Char(string='Type Name', required=True)
    brand_id = fields.Many2one('workshop_bjm.car_brand', string='Brand')

