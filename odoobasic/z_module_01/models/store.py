from odoo import models, fields

class Store(models.Model):
  _name = 'store'
  _inherit = ['abstract', 'mail.thread']
  _description = 'Stores'

  expense_ids = fields.One2many('expense', 'store_ids', string='Expenses')
  provider_ids = fields.Many2many('provider', string='Providers')