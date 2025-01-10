import xmlrpc.client

from Demos.mmapfile_demo import offset

url = 'http://127.0.0.1:8069/'
db = 'demo'
username = 'admin'
password = '1'

api_key_external = 'f19847baac47812afcf2362bfaf6a5acb8402bf6'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print("version info", common.version())

uid = common.authenticate(db, username, password, {})
if uid:
  models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
  # offset: số lượng bản ghi cần bỏ qua (từ đâu -> $value)
  # limit: số lượng bản ghi cần lấy ra (từ đâu -> $value)
  # search method
  # partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 1, 'limit': 10})
  partners = models.execute_kw(db, uid, password, 'res.partner', 'search_count',
                               [[['is_company', '=', True]]])
  # partners = models.execute_kw(db, uid, password, 'expense', 'search', [[['name', 'ilike', 'Hehe']]])
  print("->>>>", partners)

  # read method
  # partner_rec = models.execute_kw (db, uid, password, 'res.partner', 'read', [partners]})
  partner_rec = models.execute_kw(db, uid, password, 'res.partner', 'read',
                                  [partners], {'fields': ['id', 'name']})
  print("->>>>", partner_rec)
else:
  print("Authentication failed")

