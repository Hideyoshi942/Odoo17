# -*- coding: utf-8 -*-
{
  'name': "education",

  'summary': "Short (1 phrase/line) summary of the module's purpose",

  'description': """
Long description of module's purpose
    """,

  'author': "My Company",
  'website': "https://www.yourcompany.com",

  # Categories can be used to filter modules in modules listing
  # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
  # for the full list
  'category': 'Uncategorized',
  'version': '0.1',

  # any module necessary for this one to work correctly
  'depends': ['base', 'website', 'web'],

  # always loaded
  'data': [
    # 'security/ir.model.access.csv',
    'views/todo_task_views.xml',
    'views/res_partner.xml',
  ],
  # only loaded in demonstration mode
  'demo': [
    'demo/demo.xml',
  ],
  'assets': {
    # 'web.assets_frontend': [
    #   'static/src/css/education_style.css',
    #   'static/src/js/education.js',
    #   'static/src/scss/education_style.scss',
    # ],
    'web.assets_backend': [
      'education/static/src/components/*/*.js',
      'education/static/src/components/*/*.xml',
      'education/static/src/components/*/*.scss',
    ],
  }
}
