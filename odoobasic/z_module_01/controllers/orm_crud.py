from odoo import http
from odoo.http import request
class OrmCrudController(http.Controller):

  @http.route('/orm_crud', type='http', auth='public', website=True)
  def orm_crud_expense(self):
    expenses = request.env['expense'].search([])
    return request.render('z_module_01.orm_crud_template', {'expenses': expenses})