{
  'name': "Manchester City",
  'summary': "Module for football club management",
  'description': """
   What it does
   ============
   The module provides management player football features.
   Key Features
   ============
   * Player management
   * Club management
   """,
  'author': "Hideyoshi",
  'category': 'Football',
  'version': '0.1.0',
  'depends': ['base'],
  'data': [
    'security/player_security.xml',
    'security/ir.model.access.csv',
    'views/player_views.xml',
  ],
  'demo': ['demo.xml'],
}
