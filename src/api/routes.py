from flask import Flask, request, jsonify, url_for, Blueprint, current_app, session
from models import db, User, Chef
from werkzeug.exceptions import HTTPException
from flask_bcrypt import Bcrypt
from flask_session import Session
import bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
bcrypt = Bcrypt()

import cloudinary
import cloudinary.uploader
import cloudinary.api

api = Blueprint('api', __name__)


from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)

cloudinary.config(
  cloud_name = "dztgp8g6w",
  api_key = "158344581497744",
  api_secret = "a5xb9RBMOpovJEOOranrRYLWAYw"
)

class APIException(HTTPException):
    code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__(message, payload)
        if status_code is not None:
            self.code = status_code

# Login


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
    'surname': user.surname
    }
        
    token = create_access_token(identity=data, expires_delta=timedelta(minutes=1))
    return jsonify(token), 200


##----------------------------------------------------------------------------##
##---------------------------------TABLE USER---------------------------------##
##----------------------------------------------------------------------------##


#_____________________________________CRUD_____________________________________#

#___________________________________LIST USER___________________________________#
@api.route('/users', methods=['GET'])
def list_user():
    users = User.query.all()
    all_users = []
    for user in users:
        all_users.append(user.serialize())
    return jsonify(all_users)

#__________________________________CREATE USER__________________________________#
@api.route('/register', methods=['POST'])
def register_user():
    email = request.json["email"]
    password = request.json["password"]
    body = request.json
    user_exists = User.query.filter_by(email=email).first() is not None
    
    if user_exists:
        return jsonify({"error" : "User already exists"}), 409
    
    hashed_password = bcrypt.generate_password_hash(password)
    print(hashed_password)
    print(User(password))
    new_user = User(email=email , password=hashed_password , name=body['name'], surname=body['surname'], is_active=True, is_admin=False)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({
        "id" : new_user.id,
        "email" : new_user.email,
        'name': new_user.name,
        'surname': new_user.surname
        
    })
    
#__________________________________UPDATE USER__________________________________#
@api.route('/users/<int:id>' , methods=['PUT'])
def update_user(id):

    user = User.query.get(id)
    body = request.get_json()

    if "username" in body:
        user.username = body["username"]
    elif "email" in body:
        user.email = body["email"]

    db.session.commit()

    return jsonify(user.serialize())

#__________________________________DELETE USER__________________________________#
@api.route('/users/<int:id>' , methods=['DELETE'])
def delete_user(id):

    user = User.query.get(id)

    if user is None:
        raise APIException("USER DELETE", 201)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User eliminado correctamente"}), 200

##----------------------------------------------------------------------------##
##---------------------------------TABLE CHEF---------------------------------##
##----------------------------------------------------------------------------##


#_____________________________________CRUD_____________________________________#

#___________________________________LIST CHEF___________________________________#
@api.route('/chefs', methods=['GET'])
def list_chef():
    chefs = Chef.query.all()
    all_chefs = []
    for chef in chefs:
        all_chefs.append(chef.serialize())
    return jsonify(all_chefs)

#__________________________________CREATE CHEF__________________________________#
@api.route('/crear_chef' , methods=['POST'])
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

#__________________________________UPDATE CHEF__________________________________#
@api.route('/chef/<int:id>', methods=['POST'])
def update_chef(id):
    chef = Chef.query.get(id)

    image_to_load = request.files["file"]
    if not image_to_load:
        return jsonify("imagen no existe")

    result = cloudinary.uploader.upload(image_to_load)
    url = result['url']

    name = request.form["name"]
    descripcion = request.form["descripcion"]

    if name != chef.name:
        chef.name = name.lower()
    chef.imagen = url
    chef.descripcion = descripcion.lower()

    db.session.commit()

    return jsonify("ok"), 201
#__________________________________DELETE CHEF__________________________________#
@api.route('/chefs/<int:id>' , methods=['DELETE'])
def delete_chef(id):

    chef = Chef.query.get(id)

    if chef is None:
        raise APIException("CHEF DELETE", 201)

    db.session.delete(chef)
    db.session.commit()

    return jsonify({"message": "Chef eliminado correctamente"}), 200

@api.route('/')
def index():
    return 'Hello, World!'


#___________________________________LIST CHEF___________________________________#
#__________________________________CREATE CHEF__________________________________#
#__________________________________UPDATE USER__________________________________#
#__________________________________DELETE USER__________________________________#

#___________________________________LIST USER___________________________________#
#__________________________________CREATE USER__________________________________#
#__________________________________UPDATE USER__________________________________#
#__________________________________DELETE USER__________________________________#