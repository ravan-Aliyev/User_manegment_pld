from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


app1 = Flask(__name__)

Base = declarative_base()

app1.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://pld_user:user_pwd@localhost/pld_user_db'
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app1)