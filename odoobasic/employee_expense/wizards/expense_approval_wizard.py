from odoo import models, fields, api

class ExpenseApprovalWizard(models.TransientModel):
    _name = 'expense.approval.wizard'
    _description = 'Expense Approval Wizard'

    state = fields.Selection([
        ('approved', 'Approve'),
        ('rejected', 'Reject'),
    ], required=True)

    def action_apply(self):
        expense_ids = self.env['employee.expense'].browse(
            self._context.get('active_ids'))
        expense_ids.write({'state': self.state})

        if self.state == 'approved':
            expense_ids.message_post(body="Expense approved.")
        elif self.state == 'rejected':
            expense_ids.message_post(body="Expense rejected.")

