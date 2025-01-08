from odoo import http
from odoo.addons.z_football_resource.controllers.player_controller import PlayerController

class MountainController(PlayerController):
  # Kế thừa trong controllers
  @http.route('/football_resource')
  def mountain_check(self):
    # super gọi kế thừa . + hàm kế thừa
    super(MountainController, self).index()
    return 'Inherit Controller'