from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileRequired,FileField
from wtforms import BooleanField,PasswordField,StringField,RadioField,SubmitField,SelectField
from wtforms.fields.html5 import TelField
from wtforms.validators import DataRequired, Email


class Login_formcall(FlaskForm):
   email_user=StringField('Username',validators=[DataRequired(),Email()])
   password=PasswordField('Password',validators=[DataRequired()])
   remember=BooleanField('Remember me')
   submit=SubmitField('Login')

class Userform(FlaskForm):
   personal_email=StringField("Email",validators=[DataRequired()])
   dialling_num=TelField("Tel/num",validators=[DataRequired()])
   branch=RadioField("Branch",choices=[("Dev","Dev"),("Des","Des")],validators=[DataRequired()])
   occupation=SelectField("Occupations",choices=[("Work","at work"),("Freelance","freelance"),("Unemployed","no job"),("Studying","Still studying")],validators=[DataRequired()])
   company_name=StringField("Company name")
   linkedin=StringField("Linkedin",validators=[DataRequired()])
   github=StringField("Github account",validators=[DataRequired()])
   website=StringField("Personal website (portfolio)",validators=[DataRequired()])
   Submitting=SubmitField("Submit")

class Uploading(FlaskForm):
   uploadfile=FileField("upload",validators=[FileRequired(),FileAllowed(["jpg","png","pdf","txt"])])
   Submitting=SubmitField("Submit")