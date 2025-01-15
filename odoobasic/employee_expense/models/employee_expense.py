from odoo import models, fields, api

class EmployeeExpense(models.Model):
    _name = 'employee.expense'
    _description = 'Employee Expense'
    _inherit = ['mail.thread']

    name = fields.Char(string="Expense Name", required=True, tracking=True)
    # employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    amount = fields.Float(string="Amount", required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='draft', tracking=True)
    description = fields.Text(string="Description")

    def action_submit(self):
        self.state = 'submitted'

    def action_reset(self):
        self.state = 'draft'

    def open_approval_wizard(self):
        return {
            'name': 'Approve/Reject Expense',
            'type': 'ir.actions.act_window',
            'res_model': 'expense.approval.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_ids': self.ids},
        }