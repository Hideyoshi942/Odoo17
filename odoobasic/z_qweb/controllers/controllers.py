# -*- coding: utf-8 -*-
# from odoo import http


# class ZQweb(http.Controller):
#     @http.route('/z_qweb/z_qweb', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/z_qweb/z_qweb/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('z_qweb.listing', {
#             'root': '/z_qweb/z_qweb',
#             'objects': http.request.env['z_qweb.z_qweb'].search([]),
#         })

#     @http.route('/z_qweb/z_qweb/objects/<model("z_qweb.z_qweb"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('z_qweb.object', {
#             'object': obj
#         })

