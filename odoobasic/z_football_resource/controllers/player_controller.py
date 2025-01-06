import json
import werkzeug
from odoo import http
from odoo.http import request

class PlayerController(http.Controller):
  @http.route(['/z_football_resource/player', '/football_resource_two'], auth='public', type='http')
  def index(self):
    return "Hello, world"

  @http.route('/football_resource/player/<int:player_id>', auth='public', type='http')
  def player(self, player_id):
    # return "Hello %s" %str(player_id)
    return f'Hello player {player_id}'

  # @http.route('/z_football_resource', auth='public')
  # def index(self):
  #   return werkzeug.utils.redirect('http://www.google.com')

  # @http.route('/z_football_resource', auth='public')
  # def index(self):
  #   return request.redirect("web.login")

  # @http.route('/z_football_resource', auth='public', type='http')
  # def mountain_check(self):
  #   return json.dumps({
  #     "check": "check 123"
  #   })

  # @http.route('/z_football_resource', auth='public', type='http')
  # def mountain_check(self):
  #   partner = request.env['res.partner'].sudo().create({
  #     'name': 'John Doe'
  #   })
  #   return 'Partner has been created'