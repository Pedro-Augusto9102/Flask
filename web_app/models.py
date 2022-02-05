from operator import length_hint
from web_app import db

class Info(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    marca = db.Column(db.String(length=100), nullable=False)
    desc = db.Column(db.String(length=1000), nullable=False)
    img = db.Column(db.String(length=1000), nullable=False)

class Usuario(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=100), nullable=False)
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    senha = db.Column(db.String(length=100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name