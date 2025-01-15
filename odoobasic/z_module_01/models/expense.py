from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class Expense(models.Model):
  _name = 'expense'
  _inherit = ['mail.thread']
  _description = 'Product Expense'

  # trường hiển thị tên trên giao diện chi tiết về sản phẩm nếu không có sẽ sử dụng name thay thế
  # _rec_name = 'reference'

  reference = fields.Char(string="Name", required=True,
                          default=lambda self: self.env[
                            'ir.sequence'].next_by_code(
                              'expense.sequence'))
  name = fields.Char(string='Product_name', required=True)
  image = fields.Binary(string='Image', attachment=True)

  price = fields.Monetary(string="Price", currency_field="currency_id",
                          required=True, tracking=True)
  currency_id = fields.Many2one('res.currency', string="Currency",
                                required=True,
                                default=lambda self: self.env.ref('base.USD'),
                                groups='z_module_01.group_manager')
  converted_price = fields.Float(string="Converted Price",
                                 compute="_compute_converted_price")
  target_currency_id = fields.Many2one('res.currency', string="Target Currency")

  quantity = fields.Integer(string='Quantity', required=True)
  date = fields.Date(string='Date', default=fields.Date.today)
  description = fields.Html(string='Description')
  category = fields.Selection(
      [('essential', 'Essential'), ('durable ', 'Durable '),
       ('fast-moving', 'Fast-moving'), ('raw material', 'Raw material'),
       ('machinery and equipment', 'Machinery and equipment'),
       ('other', 'Other')], string='Essential', default='essential')
  state = fields.Selection(
      [('draft', 'Draft'), ('submitted', 'Submitted'), ('approved', 'Approved'),
       ('rejected', 'Rejected')], default='draft', tracking=True)
  sequence = fields.Integer(string='Sequence', default=1)

  store_ids = fields.Many2one('store', string='Store')
  provider_ids = fields.Many2one('provider', string='Provider')

  @api.constrains('price')
  def _check_price(self):
    for record in self:
      if record.price <= 0:
        raise ValidationError('Price must be greater than 0')

  @api.constrains('quantity')
  def _check_quantity(self):
    for record in self:
      if record.quantity <= 0:
        raise ValidationError('Quantity must be greater than 0')

  def action_create_expense(self):
    return {
      'name': 'Create Expense',
      'type': 'ir.actions.act_window',
      'res_model': 'expense.transient',
      'view_mode': 'form',
      'target': 'new',
    }

  def action_create_multi_expense(self):
    return {
      'name': 'Create Multi Expense',
      'type': 'ir.actions.act_window',
      'res_model': 'wizard.expense_wizard',
      'view_mode': 'form',
      'target': 'new',
    }

  def _compute_converted_price(self):
    for record in self:
      if record.currency_id and record.target_currency_id:
        # Quy đổi giá trị từ currency_id sang target_currency_id
        record.converted_price = record.currency_id._convert(
            record.price,
            record.target_currency_id,
            record.env.company,
            fields.Date.today()
        )
      else:
        record.converted_price = 0.0

  # orm
  def action_search_expense(self):
    for record in self:
      # odoo search method
      expen = self.env['expense'].search([])
      # expen.display_name
      print("Expense: ", expen)
      # # search method with and
      # expen_category_and = self.env['expense'].search(
      #     [('category', '=', 'essential'), ('state', '!=', 'draft')])
      # print("Category and State: ", expen_category_and)
      #
      # # search method with or
      # expen_category_or = self.env['expense'].search(
      #     ['|','|', ('category', '=', 'essential'), ('state', '!=', 'draft'), ('id', '=', '1')])
      # print("Category or State: ", expen_category_or)

      # search count
      # expen_category_or = self.env['expense'].search_count(
      #     ['|', ('category', '=', 'essential'), ('state', '!=', 'draft')])
      # print("Count of Category or State: ", expen_category_or)
      #
      # # ref in odoo (trả về id của bản ghi)
      # orm_ref = self.env.ref('z_module_01.seq_expense')
      # print("Ref: ", orm_ref)

      # browse - trả về bản ghi với id
      # expense_browse = self.env['expense'].browse([1, 2])
      # print("Browse: ", expense_browse)
      # for record in expense_browse:
      #   print("Browse record id: ", record.id)
      #   try:
      #     print("Browse record name: ", record.name)
      #   except Exception as e:
      #     print("Error: ", e)
      #     raise ValidationError("An error occurred: %s" % str(e))

      # exists
      # expense_exists = self.env['expense'].browse([1, 300])
      # print("Exists: ", expense_exists)
      # for record in expense_exists:
      #   if record.exists():
      #     print("Exists record id: ", record.id)
      #     print("Exists record name: ", record.name)
      #   else:
      #     print("Record does not exist")
      #     print("Record %s does not exist" % record.id)
      # print(f"Record {record.id} does not exist")
      # print("Record {} does not exist".format(record.id))

      # create
      # vals = {
      #   'name': 'New Expense',
      #   'price': 1000000,
      #   'quantity': 1,
      # }
      # new_expense = self.env['expense'].create(vals)
      # print("Create: ", new_expense)

      # write

      # record_update = self.env['expense'].browse([3])
      # if record_update.exists():
      #   record_update.write({'name': 'Updated Expense'})
      #   print("Write: ", record_update)

      # unlink
      # record_delete = self.env['expense'].browse([6])
      # if record_delete.exists():
      #   record_delete.unlink()
      #   print("Unlink: ", record_delete)
      # else:
      #   print("No expense found")

      # copy
      # record_copy = self.env['expense'].browse([1])
      # if record_copy.exists():
      #   new_expense_copy = record_copy.copy()
      #   print("Copy: ", new_expense_copy)

      # filter  là một phương thức được sử dụng để lọc các bản ghi trong một
      # recordset dựa trên điều kiện đã cho. Nó trả về một recordset mới chứa các
      # bản ghi mà thỏa mãn điều kiện lọc.
      # records = self.env['expense'].search([])  # Tìm tất cả bản ghi
      # filtered_records = records.filtered(
      #   lambda r: r.field_name == 'value')  # Lọc theo điều kiện

      # sudo là một phương thức giúp bạn bypass các quyền truy cập của người dùng
      # và thực hiện hành động như thể bạn là người dùng có quyền cao nhất
      # (superuser). Điều này rất hữu ích khi bạn muốn thao tác trên các bản ghi mà
      # không bị hạn chế bởi quyền truy cập.
      # record = self.env['expense'].sudo().browse(1)  # Truy xuất bản ghi với ID = 1

      # with_context  là một phương thức được sử dụng để thay đổi ngữ cảnh (context)
      # của các hành động trong Odoo. Ngữ cảnh có thể chứa các giá trị như ngôn ngữ,
      # thời gian, nhóm quyền hoặc bất kỳ dữ liệu bổ sung nào mà bạn muốn thay đổi
      # hoặc bổ sung trong một hành động cụ thể.

      # Tìm kiếm bản ghi với context mới
      # records = self.env['res.partner'].with_context(lang='fr_FR').search([])
      #
      # # Cập nhật trường `state` chỉ với một context đặc biệt
      # self.env['expense'].with_context(ignore_permission=True).write(
      #     {'state': 'draft'})

      # # mapper
      # partners = self.env['res.partner'].search([])
      # partners_mapped = partners.mapped('name')
      # print("Mapped: ", partners_mapped)
      #
      # # sorted (sử dụng lamda function có thể xây dựng logic tuỳ chỉnh)
      # partners_sorted = partners.sorted('name')
      # # sorted_records = self.env['expense'].search([]).sorted(
      # #   lambda rec: rec.price + rec.tax)
      # print("Sorted: ", partners_sorted)
      #
      # # filtered
      # partners_filtered = partners.filtered(lambda p: p.name == 'John')
      # print("Filtered: ", partners_filtered)
      #
      # # groupby: Nhóm các bản ghi trong RecordSet theo một hoặc nhiều trường và
      # # trả về một dictionary với khóa là giá trị của trường nhóm.
      # partners_grouping = partners_sorted.groupby('name')
      # print("Grouping: ", partners_grouping)

  @api.model
  def send_daily_sales_report(self):
    for employee in self.env['expense'].search([]):
      # Logic gửi email hoặc lưu báo cáo
      mail_values = {
        'email_to': 'unclekiet2424@gmail.com',
        'subject': 'Daily Sales Report',
        'body_html': f'Total sales for today: {employee.name, employee.price}',
      }
      mail = (self.env['mail.mail'].create(mail_values))
      mail.send()