from petfax import db
from flask_sqlalchemy import SQLAlchemy


class Fact(db.Model):
    __tablename__ = 'facts'
    id = db.Column(db.Integer, primary_key = True)
    fact = db.Column(db.Text)
    submitter = db.Column(db.String(250))
