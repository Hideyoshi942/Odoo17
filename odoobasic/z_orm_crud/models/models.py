from odoo import models, fields

class StudentUser(models.Model):
  _name = 'student.user'
  _description = 'Student'

  student_id = fields.Integer(string='Student ID')
  course = fields.Selection([('python', 'Python'), ('java', 'Java')], string='Course', default='python')
  age = fields.Integer(string='Age')
  gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')

  # Start ORM with Query Select
  def create_student_record(self):
    query = """
      INSERT INTO student_user (student_id, course, age, gender)
      VALUES (1, 'python', 20, 'male');
    """

    # Execute the query
    self.env.cr.execute(query)

  def retrieve_student_record(self):
    query = """
      SELECT * FROM student_user;
    """

    # Execute the query
    self.env.cr.execute(query)
    result = self.env.cr.fetchall()
    print(result)

  def update_student_record(self):
    query = """
      UPDATE student_user SET age = 21 WHERE student_id = 1;
    """

    # Execute the query
    self.env.cr.execute(query)

  def delete_student_record(self):
    query = """
      DELETE FROM student_user WHERE student_id = 1;
    """

    # Execute the query
    self.env.cr.execute(query)
  # End ORM with Query Select
