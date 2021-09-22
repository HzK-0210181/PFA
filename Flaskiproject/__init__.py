from flask import Flask
from secrets import token_hex
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__)
xa=token_hex(16)
app.config['SECRET_KEY']=xa
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///PFA_DB.db'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
db=SQLAlchemy(app)

login_manag=LoginManager(app)

import Flaskiproject.routes