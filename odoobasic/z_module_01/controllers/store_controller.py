from odoo import http
from odoo.http import request
import json


class StoreController(http.Controller):
  @http.route('/store/create', type='json', auth='user')
  def create_store(self, **kwargs):
    store = request.env['store'].create(kwargs)
    return json.dumps({'code': 200, 'status': 'success', 'id': store.id})

  @http.route('/store/update/<int:store_id>', type='json', auth='user')
  def update_store_id(self, store_id=None, **kwargs):
    store = request.env['store'].browse(store_id)
    if store.exists():
      store.write(kwargs)
      return json.dumps({'code': 200, 'status': 'success'})
    else:
      return json.dumps({'code': 404, 'status': 'bad request',
                         'message': 'Store not found'})

  @http.route('/store/delete', type='http', auth='user')
  def delete_store_all(self):
    store_delete_all = request.env['store'].search([])
    store_delete_all.unlink()
    return json.dumps(
        {'code': 200, 'status': 'success', 'message': 'All stores deleted'})

  @http.route('/store/delete/<int:store_id>', type='http', auth='user')
  def delete_store_id(self, store_id=None):
    store_delete = request.env['store'].browse(store_id)
    if store_delete.exists():
      store_delete.unlink()
      return json.dumps({'code': 200, 'status': 'success'})
    else:
      return json.dumps({'code': 404, 'status': 'bad request',
                         'message': 'Store not found'})

  @http.route(['/store/list', '/store'], type='http', auth='public',
              methods=['GET'], csrf=False)
  def get_list_store(self):
    stores = request.env['store'].search([])
    stores_data = [{
      'id': store.id,
      'name': store.name,
      'phone': store.phone,
      'email': store.email,
      'address': store.address,
      'description': store.description,
      'history': store.history,
      'expense_ids': [expense.name for expense in store.expense_ids],
      'provider_ids': [provider.name for provider in store.provider_ids]
    } for store in stores]

    response_data = {
      'code': 200,
      'status': 'success',
      'data': stores_data
    }

    return request.make_response(
        json.dumps(response_data),
        headers=[('Content-Type', 'application/json')]
    )

  @http.route('/store/list/<int:store_id>', type='http', auth='public',
              methods=['GET'], csrf=False)
  def get_store_id(self, store_id=None):
    store = request.env['store'].browse(store_id)
    if store.exists():
      stores_data = [{
        'id': store.id,
        'name': store.name,
        'phone': store.phone,
        'email': store.email,
        'address': store.address,
        'description': store.description,
        'history': store.history,
        'expense_ids': [expense.name for expense in store.expense_ids],
        'provider_ids': [provider.name for provider in store.provider_ids]
      }]
      response_data = {
        'code': 200,
        'status': 'success',
        'data': stores_data
      }
      return json.dumps(response_data)
    else:
      return json.dumps(
          {'code': 404, 'status': 'not found', 'message': 'Store not found'})
