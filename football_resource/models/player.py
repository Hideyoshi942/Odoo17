from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Player(models.Model):
    _name = 'player'

    # Thêm mô tả cho model:
    _description = 'Player'

    # Để sắp xếp các bản ghi (theo thứ tự trường name), theo sau đoạn code sau:
    _order = 'name'

    #Sử dụng trường code để làm tên đại diện cho bản ghi, theo sau đoạn code sau:
    # _rec_name = 'code'
    # code = fields.Char(string='Code', required=True)

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string='Image', attachment=True)
    country = fields.Char(string='Country')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    day_of_birth = fields.Datetime(string='Day of birth')
    position = fields.Char(string='Position', groups='football_resource.group_player_manager')
    height = fields.Float(string='Height')
    weight = fields.Float(string='Weight')

    @api.constrains('height', 'weight')
    def _check_positive_values(self):
      for record in self:
        if record.height <= 0:
          raise ValidationError('Height must be a positive number.')
        if record.weight <= 0:
          raise ValidationError('Weight must be a positive number.')