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

  # search trả về id, read chả về giá trị

  # read method
  # partner_rec = models.execute_kw (db, uid, password, 'res.partner', 'read', [partners]})
  # partner_rec = models.execute_kw(db, uid, password, 'res.partner', 'read',
  #                                 [partners], {'fields': ['id', 'name']})
  # print("->>>>", partner_rec)

  # search_read method
  # partner_rec = models.execute_kw(db, uid, password, 'res.partner', 'search_read',
  #                   [[['is_company', '=', True]]],
  #                   {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
  # print("->>>>", partner_rec)

  # create method
  # vals = {'name': 'Test Company', 'is_company': True}
  # partner_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [vals])
  # partner_id = models.execute_kw(db, uid, password, 'res.partner', 'create',
  #                        [{'name': "New Partner"}])
  # partner_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': 'Test Company'}])
  # print("->>>>", partner_id)

  # partners_search = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['name', '=', 'New Partner']]])
  # print("->>>>", partners_search)

  # write method
  # models.execute_kw(db, uid, password, 'res.partner', 'write', [[ids], values])
  # models.execute_kw(db, uid, password, 'res.partner', 'write', [[partners_search[0]], {'name': 'New Partner Name'}])
  # print("->>>>", "Write method")
  # partner_rec = models.execute_kw (db, uid, password, 'res.partner', 'read', [partners]})

  # partners_read = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners_search], {'fields': ['id', 'name']})
  # print("->>>>", partners_read)


  # unlink method
  # models.execute_kw(db, uid, password, 'res.partner', 'unlink', [partners_search])
  # print("->>>>", "Unlink method")

  # copy method
  # models.execute_kw(db, uid, password, 'res.partner', 'copy', [[partners_search[0]], {'name': 'Copy Partner Name'}])
  # print("->>>>", "Copy method")
  #
  # partners_search_copy = models.execute_kw(db, uid, password, 'res.partner',
  #                                     'search',
  #                                     [[['name', '=', 'Copy Partner Name']]])
  # print("->>>>", partners_search_copy)

  # fields_get method
  # fields = models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [])
  # print("->>>>", fields)


  # using with ir.model
  # models_create = models.execute_kw(db, uid, password, 'ir.model', 'create', [{
  #   'name': "Custom Model",
  #   'model': "x_custom_model",
  #   'state': 'manual',
  # }])
  # models_fields_get = models.execute_kw(db, uid, password, 'x_custom_model', 'fields_get', [],
  #                   {'attributes': ['string', 'help', 'type']})
  # print("->>>>", models_create, models_fields_get)

  # models_search = models.execute_kw(db, uid, password, 'ir.model', 'search', [[['model', '=', 'x_custom_model']]])
  #
  # models_unlink = models.execute_kw(db, uid, password, 'ir.model', 'unlink', [models_search])

  # ir.model.fields
  # id = models.execute_kw(db, uid, password, 'ir.model', 'create', [{
  #   'name': "Custom Model",
  #   'model': "x_custom",
  #   'state': 'manual',
  # }])
  # models.execute_kw(db, uid, password, 'ir.model.fields', 'create', [{
  #   'model_id': id,
  #   'name': 'x_name',
  #   'ttype': 'char',
  #   'state': 'manual',
  #   'required': True,
  # }])
  # record_id = models.execute_kw(db, uid, password, 'x_custom', 'create',
  #                               [{'x_name': "test record"}])
  # models.execute_kw(db, uid, password, 'x_custom', 'read', [[record_id]])
  # print("->>>>", id, record_id)
else:
  print("Authentication failed")

