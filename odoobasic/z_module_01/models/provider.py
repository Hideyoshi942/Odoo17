from odoo import models, fields

class Provider(models.Model):
  _name = 'provider'
  _inherit = ['abstract', 'mail.thread']
  _description = 'Provider'

  expense_ids = fields.One2many('expense', 'provider_ids', string='Expenses')
  store_ids = fields.Many2many('store', string='Stores')

