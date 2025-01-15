from odoo import models, fields

class Store(models.Model):
  _name = 'store'
  _inherit = ['abstract', 'mail.thread']
  _description = 'Stores'

  expense_ids = fields.One2many('expense', 'store_ids', string='Expenses')
  provider_ids = fields.Many2many('provider', string='Providers')

  def action_store(self):
    # new: tạo ra một bản ghi tạm thời không lưu vào csdl
    vals = {'name': 'New Store', 'phone': '0987654123'}
    record = self.env['store'].new(vals)
    print(record.name)  # 'New Expense'

    # update: Cập nhật nhiều trường trên một bản ghi. (giống với write chỉ khác là update làm việc với nhiều trường)
    record = self.env['store'].browse(1)
    record.update({'name': 'Updated Expense', 'phone': '0987654321'})

    # ensure_one: Đảm bảo rằng một phương thức chỉ hoạt động trên đúng một bản ghi. Nếu số lượng bản ghi không phải là một, sẽ sinh lỗi.
    self.ensure_one()
    print(self.name)

    # ids: Trả về danh sách các ID của các bản ghi trong recordset.
    records = self.env['store'].search([])
    print(records.ids)

    # search_read: Kết hợp việc tìm kiếm (search) và đọc (read) dữ liệu trong một lệnh duy nhất để tăng hiệu suất.
    records = self.env['store'].search_read([], ['name', 'phone'])
    print(records)

    # user_has_group: Kiểm tra xem người dùng hiện tại có thuộc một nhóm quyền nhất định hay không.
    if self.env.user.has_group('z_module_01.group_manager'):
      print("User is an manager")

