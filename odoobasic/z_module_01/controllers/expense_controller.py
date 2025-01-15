from odoo import http
from odoo.http import request
import json


class ExpenseController(http.Controller):
  @http.route('/expense/create', type='json', auth='user')
  def create_expense(self, **kwargs):
    expense = request.env['expense'].create(kwargs)
    return json.dumps({'code': 200,'status': 'success', 'id': expense.id})

  @http.route('/expense/update/<int:expense_id>', type='json', auth='user')
  def update_expense_id(self, expense_id=None, **kwargs):
    expense = request.env['expense'].browse(expense_id)
    if expense.exists():
      expense.write(kwargs)
      return json.dumps({'code': 200,'status': 'success'})
    else:
      return json.dumps({'code': 400,'status': 'bad request', 'message': 'Expense not found'})

  @http.route('/expense/delete', type='http', auth='user')
  def delete_expense_all(self):
    expense_delete_all = request.env['expense'].search([])
    expense_delete_all.unlink()

  @http.route('/expense/delete/<int:expense_id>', type='http', auth='user')
  def delete_expense_id(self, expense_id=None):
    expense_delete = request.env['expense'].browse(expense_id)
    if expense_delete.exists():
      expense_delete.unlink()
      return json.dumps({'code': 200,'status': 'success'})
    else:
      return json.dumps({'code': 400,'status': 'bad request', 'message': 'Expense not found'})

  @http.route(['/expense/list', '/expense'], type='http', auth='public',
              methods=['GET'], csrf=False)
  def get_list_expense(self):
    expenses = request.env['expense'].search([])
    expenses_data = [{
      'id': expense.id,
      'name': expense.name,
      'price': expense.price,
      'quantity': expense.quantity,
      'date': expense.date.strftime('%d-%m-%Y') if expense.date else None,
      'description': expense.description,
      'category': expense.category,
      'state': expense.state,
      'provider_ids': [provider.name for provider in expense.provider_ids],
      'store_ids': [store.name for store in expense.store_ids],
    } for expense in expenses]

    response_data = {
      'code': 200,
      'status': 'success',
      'data': expenses_data
    }

    return request.make_response(
        json.dumps(response_data),
        headers=[('Content-Type', 'application/json')]
    )

  @http.route(['/expense/list/<int:expense_id>', '/expense/<int:expense_id>'], type='http', auth='public',
              methods=['GET'], csrf=False)
  def get_expense_id(self, expense_id=None):
    expenses = request.env['expense'].browse(expense_id)
    expenses_data = [{
      'id': expense.id,
      'name': expense.name,
      'price': expense.price,
      'quantity': expense.quantity,
      'date': expense.date.strftime('%d-%m-%Y') if expense.date else None,
      'description': expense.description,
      'category': expense.category,
      'state': expense.state,
      'provider_ids': [provider.name for provider in expense.provider_ids],
      'store_ids': [store.name for store in expense.store_ids],
    } for expense in expenses]

    response_data = {
      'code': 200,
      'status': 'success',
      'data': expenses_data
    }

    return request.make_response(
        json.dumps(response_data),
        headers=[('Content-Type', 'application/json')]
    )
