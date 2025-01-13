# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class z_module_02(models.Model):
#     _name = 'z_module_02.z_module_02'
#     _description = 'z_module_02.z_module_02'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

