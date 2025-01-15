import xmlrpc.client
from odoo import http
from odoo.http import request

class ExpenseXmlController(http.Controller):
    @http.route('/expense_xml/list', type='http', auth='user', website=True)
    def render_expense_list(self):
        # Thông tin kết nối API
        url = 'http://127.0.0.1:8069/'
        db = 'demo'
        username = 'admin'
        password = '1'

        # Kết nối tới Odoo API qua xmlrpc
        common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
        uid = common.authenticate(db, username, password, {})

        if uid:
            models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

            # Gọi API để lấy danh sách các đối tượng partner
            expense_xml = models.execute_kw(
                db, uid, password, 'expense', 'search_read',
                [[]],
                {'fields': ['id', 'name', 'price', 'category'], 'limit': 10}
            )
        else:
            expense_xml = []
            print('Không thể kết nối tới Odoo API')

        # Trả dữ liệu ra giao diện template
        return request.render('z_module_01.expense_xml_template', {
            'expenses_xml': expense_xml
        })
