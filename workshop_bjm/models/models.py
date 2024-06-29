# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class workshop_bjm(models.Model):
#     _name = 'workshop_bjm.workshop_bjm'
#     _description = 'workshop_bjm.workshop_bjm'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

