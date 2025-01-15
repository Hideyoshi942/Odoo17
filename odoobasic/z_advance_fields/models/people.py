from odoo import models, fields


class PeopleAdvance(models.Model):
    _name = 'peopleadvance'
    _description = 'People Advance'

    name = fields.Char(string='Name')

    # Binary field
    cv1 = fields.Binary(string='CV 1')
    cv2 = fields.Binary(string='CV 2', attachment=False)

    # HTML field
    description = fields.Html(string='Description')
    description2 = fields.Html(string='Description 2', sanitize_tags=False)

    # Image field
    avatar = fields.Image(string='Avatar', max_width=1920, max_height=1920)

    # Selection field
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

    # Text field
    information = fields.Text(string='Information')