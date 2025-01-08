{
    'name': 'Employee Expense Management',
    'summary': 'Manage employee expenses and approvals',
    'version': '1.0',
    'author': 'Hideyoshi',
    'category': 'Human Resources',
    'depends': ['base', 'mail'],
    'data': [
        'security/employee_expense_security.xml',
        'security/ir.model.access.csv',
        'views/employee_expense_views.xml',
        'views/employee_expense_wizard_views.xml',
    ],
    'images': ['static/description/Expense-Policy-1.png'],
    'license': 'LGPL-3',
}
