from odoo import http
from odoo.http import request
import json


class OrmCrudController(http.Controller):

  @http.route('/orm_crud', type='http', auth='public', website=True)
  def orm_crud_expense(self):
    expenses = request.env['expense'].search([])
    print(expenses)
    return request.render('z_module_01.orm_crud_template',
                          {'expenses': expenses})

  # API để trả về dữ liệu expense dưới dạng JSON
  @http.route(['/orm_crud_api', '/json_api'], type='http', auth='public',
              methods=['GET'],
              csrf=False)
  def orm_crud_expense_api(self):
    expenses = request.env['expense'].search([])  # Lấy tất cả bản ghi expense
    expenses_data = [{
      'id': expense.id,
      'name': expense.name,
      'price': expense.price,
    } for expense in expenses]  # Lấy dữ liệu cần thiết từ mỗi expense

    # Trả về dữ liệu dạng JSON
    response_data = {
      'status': 'success',
      'data': expenses_data
    }

    return request.make_response(
        json.dumps(response_data),  # Chuyển đổi dữ liệu thành JSON
        headers=[('Content-Type', 'application/json')]
        # Đảm bảo header trả về là application/json
    )

  # API để trả về dữ liệu expense dưới dạng JSON
  @http.route('/orm_json', type='http', auth='user', methods=['GET'],
              csrf=False)
  def orm_crud_expense_api_http(self, **kwargs):
    expenses = request.env['expense'].search([])
    expenses_data = [{
      'id': expense.id,
      'name': expense.name,
      'price': expense.price,
    } for expense in expenses]

    return request.make_response(
        json.dumps({
          "status": "success",
          "data": expenses_data,
        }),
        headers={'Content-Type': 'application/json'}
    )
