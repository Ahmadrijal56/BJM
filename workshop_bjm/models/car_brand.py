from odoo import models, fields, api

class CarBrand(models.Model):
    _name = 'workshop_bjm.car_brand'
    _description = 'Car Brands'

    name = fields.Char(string='Brand Name', required=True)
    type_ids = fields.One2many('workshop_bjm.car_type', 'brand_id', string='Types')
