from odoo import http
from odoo.http import request
import json

class OrmCrudController(http.Controller):

  @http.route('/orm_crud', type='http', auth='public', website=True)
  def orm_crud_expense(self):
    expenses = request.env['expense'].search([])
    return request.render('z_module_01.orm_crud_template', {'expenses': expenses})

  @http.route('/orm_crud_api', type='http', auth='user  ', methods=['GET'],
              csrf=False)
  def orm_crud_expense_api(self):
    expenses = request.env['expense'].search([])
    expenses_data = [{
      'id': expense.id,
      'name': expense.name,
      'price': expense.price,
    } for expense in expenses]

    # Trả về JSON response
    return request.make_response(
        json.dumps({'status': 'success', 'data': expenses_data}),
        headers=[('Content-Type', 'application/json')]
    )
