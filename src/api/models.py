from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
    
class Chef(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    descripcion = db.Column(db.String(200), unique=True, nullable=False)
    imagen = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Chef %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.imagen,
            "description": self.descripcion,
        }