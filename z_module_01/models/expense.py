from odoo import models, fields


class Expense(models.Model):
  _name = 'expense'
  _description = 'Project check knowledge about odoo'

  name = fields.Char(string='Product_name', required=True)
  image = fields.Binary(string='Image', attachment=True)
  price = fields.Monetary(string="Price", currency_field="currency_id",
                          required=True)
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
