from odoo import http
from odoo.http import request

class ExpenseReportController(http.Controller):

    @http.route('/expense_report', type='http', auth='user')
    def get_expense_report(self):
        expenses = request.env['employee.expense'].search([])
        html = "<h1>Employee Expenses</h1>"
        for expense in expenses:
            html += f"<p>{expense.name}: ${expense.amount}</p>"
        return request.make_response(html)
