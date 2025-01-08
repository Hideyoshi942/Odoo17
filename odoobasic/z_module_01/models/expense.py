from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Expense(models.Model):
  _name = 'expense'
  _inherit = ['mail.thread']
  _description = 'Product Expense'

  # trường hiển thị tên trên giao diện chi tiết về sản phẩm nếu không có sẽ sử dụng name thay thế
  # _rec_name = 'reference'

  reference = fields.Char(string="Name", required=True,
                          default=lambda self: self.env[
                            'ir.sequence'].next_by_code(
                              'expense.sequence'))
  name = fields.Char(string='Product_name', required=True)
  image = fields.Binary(string='Image', attachment=True)
  price = fields.Monetary(string="Price", currency_field="currency_id",
                          required=True, tracking=True)
  currency_id = fields.Many2one('res.currency', string="Currency",
                                required=True,
                                default=lambda self: self.env.ref('base.USD'), groups='z_module_01.group_manager')
  quantity = fields.Integer(string='Quantity', required=True)
  date = fields.Date(string='Date', default=fields.Date.today)
  description = fields.Html(string='Description', required=True)
  category = fields.Selection(
      [('essential', 'Essential'), ('durable ', 'Durable '),
       ('fast-moving', 'Fast-moving'), ('raw material', 'Raw material'),
       ('machinery and equipment', 'Machinery and equipment'),
       ('other', 'Other')], string='Essential', default='essential')
  state = fields.Selection(
      [('draft', 'Draft'), ('submitted', 'Submitted'), ('approved', 'Approved'),
       ('rejected', 'Rejected')], default='draft', tracking=True)
  sequence = fields.Integer(string='Sequence', default=1)

  store_ids = fields.Many2one('store', string='Store')
  provider_ids = fields.Many2one('provider', string='Provider')



  @api.constrains('price')
  def _check_price(self):
    for record in self:
      if record.price <= 0:
        raise ValidationError('Price must be greater than 0')

  @api.constrains('quantity')
  def _check_quantity(self):
    for record in self:
      if record.quantity <= 0:
        raise ValidationError('Quantity must be greater than 0')

  def action_create_expense(self):
    return {
      'name': 'Create Expense',
      'type': 'ir.actions.act_window',
      'res_model': 'expense.transient',
      'view_mode': 'form',
      'target': 'new',
    }