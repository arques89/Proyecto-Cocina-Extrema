from flask import Flask, request, jsonify, url_for, Blueprint, current_app
from models import db, User, Chef
from werkzeug.exceptions import HTTPException

import  bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

import cloudinary
import cloudinary.uploader
import cloudinary.api

api = Blueprint('api', __name__)

cloudinary.config( 
  cloud_name = "dztgp8g6w", 
  api_key = "158344581497744", 
  api_secret = "a5xb9RBMOpovJEOOranrRYLWAYw" 
)

routes = Blueprint('routes', __name__)

class APIException(HTTPException):
    code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__(message, payload)
        if status_code is not None:
            self.code = status_code


@routes.route('/users', methods=['GET']) 
def list_user():
    users = User.query.all()
    all_users = []
    for user in users:
        all_users.append(user.serialize())
    return jsonify(all_users)

@routes.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    # Obtener los datos del formulario si están presentes
    data = request.json
    if not data:
        data = request.form

    # Verificar si 'username' y 'email' están presentes
    if 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Se requiere el nombre de usuario y el correo electrónico.'}), 400

    # Crear un nuevo objeto de usuario
    nuevo_usuario = User(username=data['username'], email=data['email'])

    # Agregar el nuevo usuario a la sesión y guardar en la base de datos
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'message': 'Usuario creado correctamente.'}), 201

@routes.route('/chefs', methods=['GET']) 
def list_chef():
    chefs = Chef.query.all()
    all_chefs = []
    for chef in chefs:
        all_chefs.append(chef.serialize())
    return jsonify(all_chefs)

@routes.route('/crear_chef' , methods=['POST'])
def crear_chef():

    imagen_to_load = request.files["imagen"]
    if not imagen_to_load:
        return jsonify("imagen no existe")


    result = cloudinary.uploader.upload(imagen_to_load)
    print(result)
    url=result['url']
    print("esta es la url..................",url)

    # dataUser = get_jwt_identity()
    name=request.form["name"]
    descripcion=request.form["descripcion"]

    chef_check_name = Chef.query.filter_by(name=name).first()
    if chef_check_name != None:
        raise APIException('Ya existe este nombre de chef')
    chef = Chef(
        name=name.lower(),
        imagen=url,
        descripcion=descripcion.lower(),
    )

    db.session.add(chef)
    db.session.commit()
    return jsonify("ok"), 201
    
@routes.route('/chefs/<int:id>' , methods=['DELETE'])
def delete_chef(id):

    chef = Chef.query.get(id)

    if chef is None:
        raise APIException("CHEF DELETE", 201)

    db.session.delete(chef)
    db.session.commit()

    return jsonify({"message": "Chef eliminado correctamente"}), 200

@routes.route('/')
def index():
    return 'Hello, World!'