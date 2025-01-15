from odoo import models

class Dog(models.Model):
  _name = 'dog'
  _inherit = 'animal.abstract'

  def _sound(self):
    super(Dog, self)._sound()
    return 'Gâu Gâu'

  def action_create_dog(self):
    return {
      'name': 'Create Dog',
      'type': 'ir.actions.act_window',
      'res_model': 'dog',
      'view_mode': 'form',
      'target': 'new',
    }