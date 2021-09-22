from flask import render_template,redirect, session,url_for,request,flash
from werkzeug.utils import secure_filename
from Flaskiproject import app
from Flaskiproject.forms import Login_formcall, Uploading,Userform
from Flaskiproject.models import *
import os
import pathlib

from datetime import datetime

@app.route('/',methods = ["GET","POST"])
def login():
   form = Login_formcall()
   if form.is_submitted():
      if form.email_user.data.split('@')[1] == "direwa.com":
         if Admin.query.filter_by(email = form.email_user.data,password = form.password.data).first():
            current_admin = Admin.query.filter_by(email=form.email_user.data).first()
            session.permanent = True
            session["Admin"] = current_admin.id
            return redirect(url_for('admin'))
      elif form.email_user.data.split('@')[1] == "ecolewa.com":
         if Students.query.filter_by(email = form.email_user.data,password = form.password.data).first():
            current_student = Students.query.filter_by(email = form.email_user.data).first()
            session.permanent = True
            session["student"] = current_student.id
            return redirect(url_for('user'))
   return render_template("Layout_log.html",form=form)


@app.route('/admin')
def admin():
   date = datetime.now()
   eleganter_date = date.strftime("%A %d %B %Y")
   return render_template('Admin/dashboard.html',date = eleganter_date)
@app.route('/admin/profiles')
def show_profiles():
   date = datetime.now()
   eleganter_date = date.strftime("%A %d %B %Y")
   print(Students.query.get(1))
   return render_template("Admin/profiles.html",Students = Students.query.all(),date=eleganter_date)
@app.route('/user',methods = ["GET","POST"])
def user():
   if "student" in session:
      current_student = Students.query.get(session['student'])
      form = Uploading()
      ext = {'.jpg', '.png', '.pdf','.txt'}
      """
      here it checks if the student is in the session then later on it get's the student's data in the database then getting the form that will be rendered in the template and defining the extension 
      """
      if form.validate_on_submit() and request.method == "POST":
         file = request.files['uploadfile']
         if pathlib.Path(file.filename).suffix.lower() in ext :
            current_path = os.getcwd()
            if not os.path.exists(f"{current_path}/Flaskiproject/static/fileupload/{current_student.fullname}"):
               print(current_path)
               os.mkdir(os.path.join(current_path + "/Flaskiproject/static/fileupload",current_student.fullname))
               uploaded_file = secure_filename(file.filename)
               file.save(os.path.join(current_path + f"/Flaskiproject/static/fileupload/{current_student.fullname}",uploaded_file))
            else:
               uploaded_file = secure_filename(file.filename)
               file.save(os.path.join(current_path + f"/Flaskiproject/static/fileupload/{current_student.fullname}",uploaded_file))
         else:
            flash(" we don't allow this file extension ")
         return redirect(url_for('user'))
   else:
      return redirect(url_for("login"))
   return render_template("User/Homepage.html",student = current_student,form = form)


@app.route('/user/edit_profile',methods=["GET","POST"])
def get_data():
   if "student" in session:
      current_student = Students.query.get(session['student'])
      formi = Userform()
      if formi.validate_on_submit():
         current_student.personal_email = formi.personal_email.data
         current_student.dialling_num = formi.dialling_num.data
         current_student.branch = formi.branch.data
         current_student.occupation = formi.occupation.data
         current_student.company_name = formi.company_name.data
         current_student.linkedin = formi.linkedin.data
         current_student.github = formi.github.data
         current_student.website = formi.website.data
         db.session.commit()
         return redirect(url_for('user'))
   else:
      return redirect(url_for('login'))
   return render_template("User/edit_page.html",form = formi)


@app.route('/logout')
def logout():
   session.pop("student",None)
   return redirect(url_for('login'))
