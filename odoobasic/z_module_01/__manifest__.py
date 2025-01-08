{
  'name': 'Project Myself',
  'summary': 'Project module 01',
  'version': '1.0',
  'author': 'Hideyoshi',
  'category': 'Project',
  'depends': ['base','mail'],
  'data': [
    'security/ir.model.access.csv',
    'security/user_management_views.xml',
    'data/sequence.xml',
    'views/orm_crud_views.xml',
    'views/expense_views.xml',
    'views/store_views.xml',
    'views/provider_views.xml',
    'views/menu_root_views.xml',
  ],
  'assets': {
    'web.assets_backend': [
      'z_module_01/static/scss/product_template.scss',
    ],
  },
  'license': 'LGPL-3',
}