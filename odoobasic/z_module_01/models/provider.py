from odoo import models, fields

class Provider(models.Model):
  _name = 'provider'
  _inherit = ['abstract', 'mail.thread']
  _description = 'Provider'

  # chir sử dụng với các trường có mỗi quan hệ, dùng để tra cứu dữ liệu từ các trường được nối với nhau
  _rec_names_search = ['phone', 'store_ids']

  expense_ids = fields.One2many('expense', 'provider_ids', string='Expenses')
  store_ids = fields.Many2many('store', string='Stores')

  def action_provider(self):

    # external_id: trả về extenal_id của model
    # record = self.env['ir.ui.view'].browse(1)
    # external_id = record.get_external_id()
    # print(external_id)

    # get_metadata: Lấy metadata của các bản ghi như create_date, create_uid, write_date, write_uid.
    # record = self.env['provider'].browse(1)
    # metadata = record.get_metadata()
    # print(metadata)

    # read: Đọc dữ liệu của các trường trên bản ghi.
    # records = self.env['provider'].search([])
    # data = records.read(['name', 'address', 'phone'])
    # print(data)

    # fields_get: Trả về thông tin của các trường trong mô hình.
    # fields_info = self.env['provider'].fields_get(['name', 'address', 'phone'],
    #                                              attributes=['string', 'type'])
    # print(fields_info)

    # read_group: Đọc và nhóm dữ liệu theo các trường cụ thể.
    result = self.env['provider'].read_group(
        domain=[],
        fields=['address', 'name'],
        groupby=['name']
    )
    print(result)

    # # get_formview_action: Trả về action để mở form view cho bản ghi hiện tại.
    # record = self.env['provider'].browse(1)
    # action = record.get_formview_action()
    # print(action)
    #
    # # get_formview_id: Trả về ID của form view mặc định cho mô hình.
    # form_view_id = self.env['provider'].get_formview_id()
    # print(form_view_id)
    #
    # # user_has_group: Kiểm tra xem người dùng hiện tại có thuộc một nhóm quyền nhất định hay không.
    # if self.env.user.has_group('base.group_user'):
    #   print("User is in group User")

