# -*- coding: utf-8 -*-
# from odoo import http


# class ZModule02(http.Controller):
#     @http.route('/z_module_02/z_module_02', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/z_module_02/z_module_02/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('z_module_02.listing', {
#             'root': '/z_module_02/z_module_02',
#             'objects': http.request.env['z_module_02.z_module_02'].search([]),
#         })

#     @http.route('/z_module_02/z_module_02/objects/<model("z_module_02.z_module_02"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('z_module_02.object', {
#             'object': obj
#         })

