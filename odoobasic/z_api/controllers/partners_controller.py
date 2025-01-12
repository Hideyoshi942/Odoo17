from odoo import http
from odoo.http import request

class MyApiController(http.Controller):

  @http.route('/api/partners', type='json', auth='user', methods=['GET'],
              csrf=False)
  def get_partners(self):
    partners = request.env['res.partner'].search([])
    return {"status": 200,
            "data": [{"id": p.id, "name": p.name} for p in partners]}

  @http.route('/api/partners', type='json', auth='user', methods=['POST'],
              csrf=False)
  def create_partner(self, **kwargs):
    vals = {
      'name': kwargs.get('name'),
      'email': kwargs.get('email'),
      'phone': kwargs.get('phone'),
    }
    partner = request.env['res.partner'].create(vals)
    return {"status": 201, "id": partner.id}

  @http.route('/api/partners/<int:partner_id>', type='json', auth='user',
              methods=['PUT'], csrf=False)
  def update_partner(self, partner_id, **kwargs):
    partner = request.env['res.partner'].browse(partner_id)
    if not partner.exists():
      return {"status": 404, "error": "Partner not found"}
    partner.write(kwargs)
    return {"status": 200, "message": "Partner updated"}

  @http.route('/api/partners/<int:partner_id>', type='json', auth='user',
              methods=['DELETE'], csrf=False)
  def delete_partner(self, partner_id):
    partner = request.env['res.partner'].browse(partner_id)
    if not partner.exists():
      return {"status": 404, "error": "Partner not found"}
    partner.unlink()
    return {"status": 200, "message": "Partner deleted"}
