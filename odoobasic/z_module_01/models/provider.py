from odoo import models, fields

class Provider(models.Model):
  _name = 'provider'
  _inherit = ['abstract', 'mail.thread']
  _description = 'Provider'

  # chir sử dụng với các trường có mỗi quan hệ, dùng để tra cứu dữ liệu từ các trường được nối với nhau
  _rec_names_search = ['phone', 'store_ids']

  expense_ids = fields.One2many('expense', 'provider_ids', string='Expenses')
  store_ids = fields.Many2many('store', string='Stores')

