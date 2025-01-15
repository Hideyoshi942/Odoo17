from odoo import models, fields

class AbstractModel(models.AbstractModel):
  _name = 'animal.abstract'
  _description = 'Animal Abstract'

  name = fields.Char(string='Name', required=True)
  gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
  color = fields.Char(string='Color')
  age = fields.Integer(string='Age')

  def _sound(self):
    pass