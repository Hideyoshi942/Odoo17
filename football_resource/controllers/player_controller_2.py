from odoo import http
from odoo.addons.football_resource.controllers.player_controller import PlayerController

class MountainController(PlayerController):
  # Kế thừa trong controller
  @http.route('/football_resource')
  def mountain_check(self):
    # super gọi kế thừa . + hàm kế thừa
    super(MountainController, self).index()
    return 'Inherit Controller'