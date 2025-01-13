from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)


class AuthController(http.Controller):

  @http.route('/auth/login', type='json', auth='none', csrf=False,
              methods=['Post'])
  def login(self, **kw):
    """
    API Login: Kiểm tra thông tin đăng nhập và trả về session token nếu thành công.
    """
    _logger.info("Login attempt with params: %s", kw)
    email = kw.get('email')
    password = kw.get('password')

    if not email or not password:
      return {
        'code': 400,
        'status': 'error',
        'message': 'Email và mật khẩu là bắt buộc'
      }

    try:
      dbname = request.env.cr.dbname
      uid = request.session.authenticate(dbname, email, password)

      if uid:
        user = request.env['res.users'].sudo().browse(uid)
        return {
          'code': 200,
          'status': 'success',
          'message': 'Đăng nhập thành công',
          'session_id': request.session.sid,
          'user_id': user.id,
          'user_name': user.name
        }
      else:
        return {
          'code': 401,
          'status': 'error',
          'message': 'Email hoặc mật khẩu không đúng'
        }
    except Exception as e:
      _logger.error("Login error: %s", str(e))
      return {
        'code': 500,
        'status': 'error',
        'message': 'Lỗi hệ thống'
      }

  @http.route('/auth/logout', type='json', auth='user', csrf=False,
              methods=['POST'])
  def logout(self, **kw):
    """
    API Logout: Đăng xuất và hủy session người dùng.
    """
    try:
      request.session.logout()
      return {
        'code': 200,
        'status': 'success',
        'message': 'Đăng xuất thành công'
      }
    except Exception as e:
      _logger.error("Logout error: %s", str(e))
      return {
        'code': 500,
        'status': 'error',
        'message': 'Lỗi hệ thống'
      }

  @http.route('/auth/check_session', type='json', auth='user', csrf=False,
              methods=['GET'])
  def check_session(self, **kw):
    """
    API Check Session: Kiểm tra trạng thái đăng nhập của người dùng.
    """
    try:
      user = request.env.user
      if user and not user._is_public():
        return {
          'code': 200,
          'status': 'success',
          'message': 'Đã đăng nhập',
          'user_id': user.id,
          'user_name': user.name
        }
      else:
        return {
          'code': 401,
          'status': 'error',
          'message': 'Người dùng chưa đăng nhập'
        }
    except Exception as e:
      _logger.error("Check session error: %s", str(e))
      return {
        'code': 500,
        'status': 'error',
        'message': 'Lỗi hệ thống'
      }

  @http.route('/auth/signup', type='json', auth='none', csrf=False,
              methods=['POST'])
  def signup(self, **kw):
    """
    API Signup: Đăng ký tài khoản người dùng mới.
    """
    _logger.info("Signup attempt with params: %s", kw)
    email = kw.get('email')
    password = kw.get('password')
    confirm_password = kw.get('confirm_password')
    name = kw.get('name')

    # Kiểm tra dữ liệu đầu vào
    if not email or not password or not name or not confirm_password:
      return {
        'code': 400,
        'status': 'error',
        'message': 'Tên, email, mật khẩu và mật khẩu nhập lại là bắt buộc'
      }

    # Kiểm tra mật khẩu
    if password != confirm_password:
      return {
        'code': 400,
        'status': 'error',
        'message': 'Mật khẩu và mật khẩu nhập lại không khớp'
      }

    try:
      user_model = request.env['res.users'].sudo()
      partner_model = request.env['res.partner'].sudo()

      existing_user = user_model.search([('login', '=', email)])
      if existing_user:
        return {
          'code': 400,
          'status': 'error',
          'message': 'Email đã được sử dụng'
        }

      partner = partner_model.create({
        'name': name,
        'email': email,
      })

      company_id = 1

      new_user = user_model.create({
        'name': name,
        'login': email,
        'password': password,
        'company_id': company_id,
        'company_ids': [(4, company_id)],
        'partner_id': partner.id,
        'active': True,
        'groups_id': [(6, 0, [request.env.ref('base.group_user').id])],
      })

      return {
        'code': 200,
        'status': 'success',
        'message': 'Đăng ký thành công',
        'user_id': new_user.id
      }

    except Exception as e:
      _logger.error("Signup error: %s", str(e))

      # Nếu có lỗi với transaction, thử xử lý lại
      if request.cr.dbname:
        try:
          request.cr.rollback()  # Hủy bỏ transaction lỗi
        except Exception as rollback_error:
          _logger.error("Rollback failed: %s", str(rollback_error))

      return {
        'code': 500,
        'status': 'error',
        'message': 'Lỗi hệ thống'
      }
