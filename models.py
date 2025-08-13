from db import db

class User(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(40), unique=True, nullable=False)
    nome = db.Column(db.String(40), nullable=False)
    senha = db.Column(db.String(250), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
