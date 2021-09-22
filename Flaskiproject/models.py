from Flaskiproject import db,login_manag
from flask_login import UserMixin

@login_manag.user_loader
def load_student(user_id):
    return Students.get(user_id)
@login_manag.user_loader
def load_Admin(user_id):
    return Admin.get(user_id)


class Admin(db.Model,UserMixin):
   id=db.Column(db.Integer(),primary_key=True)
   fullname=db.Column(db.String(50),unique=True,nullable=False)
   email=db.Column(db.String,unique=True,nullable=False)
   password=db.Column(db.String(),unique=True,nullable=False)

   def __repr__(self):
      return f'Admin:{Admin.id} {Admin.fullname} {Admin.dialling_num} {Admin.branch}'

   def __init__(self,fullname,email,password):
      self.fullname=fullname
      self.email=email
      self.password=password


class Students(db.Model,UserMixin):
   id=db.Column(db.Integer(),primary_key=True)
   fullname=db.Column(db.String(50),unique=True,nullable=False)
   email=db.Column(db.String,unique=True,nullable=False)
   personal_email=db.Column(db.String,unique=True)
   password=db.Column(db.String(),unique=True,nullable=False)
   dialling_num=db.Column(db.String(),unique=True)
   branch=db.Column(db.String())
   occupation=db.Column(db.String())
   company_name=db.Column(db.String())
   linkedin=db.Column(db.String())
   github=db.Column(db.String())
   website=db.Column(db.String())

   def __init__(self,fullname,email,personal_email,password,dialling_num,branch,occupation,company_name,linkedin,github,website):
      self.fullname=fullname
      self.email=email
      self.personal_email=personal_email
      self.password=password
      self.dialling_num=dialling_num
      self.branch=branch
      self.occupation=occupation
      self.company_name=company_name
      self.linkedin=linkedin
      self.github=github
      self.website=website

   def __repr__(self):
      return f'Student:{Students.id} {Students.fullname} {Students.dialling_num} {Students.branch}'