# -*- coding: utf-8 -*-
# from odoo import http


# class WorkshopBjm(http.Controller):
#     @http.route('/workshop_bjm/workshop_bjm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/workshop_bjm/workshop_bjm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('workshop_bjm.listing', {
#             'root': '/workshop_bjm/workshop_bjm',
#             'objects': http.request.env['workshop_bjm.workshop_bjm'].search([]),
#         })

#     @http.route('/workshop_bjm/workshop_bjm/objects/<model("workshop_bjm.workshop_bjm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('workshop_bjm.object', {
#             'object': obj
#         })

