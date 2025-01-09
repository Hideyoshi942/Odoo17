from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ExpenseWizard(models.TransientModel):
  _name = 'wizard.expense_wizard'
  _description = 'Expense Wizard'

  expense_lines = fields.Many2one('expense.transient', string='Expense Lines')

  def action_create_expenses(self):
    """Tạo nhiều bản ghi Expense từ dữ liệu trong Wizard"""
    expense_vals = []
    for line in self.expense_lines:
      if line.price <= 0:
        raise ValidationError("Price must be greater than 0")
      if line.quantity <= 0:
        raise ValidationError("Quantity must be greater than 0")
      expense_vals.append({
        'name': line.name,
        'image': line.image,
        'price': line.price,
        'quantity': line.quantity,
        'date': line.date,
        'description': line.description,
        'category': line.category,
        'store_ids': line.store_ids.id,
        'provider_ids': line.provider_ids.id,
      })
    # Sử dụng create multi-record
    self.env['expense'].create(expense_vals)
    print("Error")
