from flask import request, jsonify
from models import User  # Importa el modelo de usuario
from flask_jwt_extended import create_access_token  # Para crear tokens de acceso
from flask_bcrypt import Bcrypt  # Para el hashing de contraseñas
from datetime import timedelta
from routes import api

bcrypt = Bcrypt()  # Instancia de Bcrypt para el hashing de contraseñas

delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)

@api.route('/login', methods=['POST'])
def login_user():
    email = request.json["email"]
    password = request.json["password"]
    
    user = User.query.filter_by(email=email).first()
    
    if user is None:
        return jsonify({"error": "Unauthorized, not user"}), 401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Unauthorized, password error"}), 401
    
    data = {
    "id": user.id,
    'email': user.email,
    'name': user.name,
    'surname': user.surname,
    'is_active' : user.is_active,
    'is_admin' : user.is_admin,
    
    }
 
    token = create_access_token(identity=data, expires_delta=timedelta(minutes=1))
    
    return jsonify({"token": token}), 200