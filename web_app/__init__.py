from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tecnocar.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Pedro1997tecnocar@localhost/usuario'
app.config['SECRET_KEY'] = '84548a24b0c24ef85082e2ed'
db = SQLAlchemy(app)    

from web_app import routes