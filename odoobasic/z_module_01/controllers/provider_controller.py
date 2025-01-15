from odoo import http
from odoo.http import request
import json


class ProviderController(http.Controller):
  @http.route('/provider/create', type='json', auth='user', methods=['post'])
  def create_provider(self, **kwargs):
    provider = request.env['provider'].create(kwargs)
    return json.dumps({'code': 200, 'status': 'success', 'id': provider.id})

  @http.route('/provider/update/<int:provider_id>', type='json', auth='user',
              methods=['put'])
  def update_provider_id(self, provider_id=None, **kwargs):
    provider = request.env['provider'].browse(provider_id)
    if provider.exists():
      provider.write(kwargs)
      return json.dumps({'code': 200, 'status': 'success'})
    else:
      return json.dumps({'code': 404, 'status': 'bad request',
                         'message': 'Provider not found'})

  @http.route('/provider/delete', type='http', auth='user', methods=['delete'])
  def delete_provider_all(self):
    provider_delete_all = request.env['provider'].search([])
    provider_delete_all.unlink()
    return json.dumps(
        {'code': 200, 'status': 'success', 'message': 'All providers deleted'})

  @http.route('/provider/delete/<int:provider_id>', type='http', auth='user',
              methods=['delete'])
  def delete_provider_id(self, provider_id=None):
    provider_delete = request.env['provider'].browse(provider_id)
    if provider_delete.exists():
      provider_delete.unlink()
      return json.dumps({'code': 200, 'status': 'success'})
    else:
      return json.dumps({'code': 404, 'status': 'bad request',
                         'message': 'Provider not found'})

  @http.route(['/provider/list', '/provider'], type='http', auth='public',
              methods=['GET'], csrf=False)
  def get_list_provider(self):
    providers = request.env['provider'].search([])
    providers_data = [{
      'id': provider.id,
      'name': provider.name,
      'phone': provider.phone,
      'email': provider.email,
      'address': provider.address,
      'description': provider.description,
      'history': provider.history,
      'expense_ids': [expense.name for expense in provider.expense_ids],
      'store_ids': [store.name for store in provider.store_ids]
    } for provider in providers]

    response_data = {
      'code': 200,
      'status': 'success',
      'data': providers_data
    }

    return request.make_response(
        json.dumps(response_data),
        headers=[('Content-Type', 'application/json')]
    )

  @http.route('/provider/list/<int:provider_id>', type='http', auth='public',
              methods=['GET'], csrf=False)
  def get_provider_id(self, provider_id=None):
    provider = request.env['provider'].browse(provider_id)
    if provider.exists():
      providers_data = [{
        'id': provider.id,
        'name': provider.name,
        'phone': provider.phone,
        'email': provider.email,
        'address': provider.address,
        'description': provider.description,
        'history': provider.history,
        'expense_ids': [expense.name for expense in provider.expense_ids],
        'store_ids': [store.name for store in provider.store_ids]
      }]
      response_data = {
        'code': 200,
        'status': 'success',
        'data': providers_data
      }
      return json.dumps(response_data)
    else:
      return json.dumps(
          {'code': 404, 'status': 'not found', 'message': 'Provider not found'})
