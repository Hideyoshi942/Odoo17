from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError

class AbstractModel(models.AbstractModel):
  _name = 'abstract'
  _description = 'Abstract Model'

  name = fields.Char(string='Name', required=True)
  phone = fields.Char(string='Phone', required=True)
  email = fields.Char(string='Email', required=True)
  address = fields.Char(string='Address', required=True)
  description = fields.Html(string='Description')
  history = fields.Html(string='History')

  @api.constrains('email')
  def _check_email(self):
    for record in self:
      email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
      if not re.match(email_regex, record.email):
        raise ValidationError('Invalid email address')

  @api.constrains('phone')
  def _check_phone(self):
    for record in self:
      if not record.phone.isdigit():
        raise ValidationError('Invalid phone number')
      if len(record.phone) != 10:
        raise ValidationError('Phone number should be 10 digits')

