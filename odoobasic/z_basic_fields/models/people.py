from string import digits
from reportlab.graphics.transform import translate
from odoo import models, fields

class People(models.Model):
  _name = 'people'
  _description = 'People'

  # required-bắt buộc, size-kích thước tối thiểu, trim-xoá khoảng trắng hiển thị trên view (không xoá trong db, gtri mặc định = true), translate-hỗ trợ bản dịch
  name = fields.Char(string='Name', required=True, size=8, trim=True, translate=True)

  # Check box - available (boolean mặc định là false)
  available = fields.Boolean(string='Available')

  # float digits: số đầu tổng số, số sau là giá trị thập phân
  height = fields.Float(string='Height', digits=(4, 2))

  age = fields.Integer(string='Age')
