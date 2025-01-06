from odoo import models, fields, api


class Expense(models.Model):
  _name = 'expense'
  _inherit = ['mail.thread']
  _description = 'Product Expense'


  # trường hiển thị tên trên giao diện chi tiết về sản phẩm nếu không có sẽ sử dụng name thay thế
  # _rec_name = 'reference'

  reference = fields.Char(string="Name", required=True,
                     default=lambda self: self.env['ir.sequence'].next_by_code(
                       'expense.sequence'))
  name = fields.Char(string='Product_name', required=True)
  image = fields.Binary(string='Image', attachment=True)
  price = fields.Monetary(string="Price", currency_field="currency_id",
                          required=True, tracking=True)
  currency_id = fields.Many2one('res.currency', string="Currency",
                                required=True, default=lambda self: self.env.ref('base.USD'))
  quantity = fields.Integer(string='Quantity', required=True)
  date = fields.Date(string='Date', default=fields.Date.today)
  description = fields.Html(string='Description', required=True)
  category = fields.Selection(
      [('essential', 'Essential'), ('durable ', 'Durable '),
       ('fast-moving', 'Fast-moving'), ('raw material', 'Raw material'),
       ('machinery and equipment', 'Machinery and equipment'),
       ('other', 'Other')], string='Essential', default='essential')
