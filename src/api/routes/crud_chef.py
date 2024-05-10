from flask import request, jsonify  # Para manejar las solicitudes HTTP y las respuestas JSON
from models import db, Chef  # Para acceder al modelo de datos de Chef y la instancia de base de datos
import cloudinary.uploader  # Para cargar imágenes a Cloudinary
from . import cloudinary  # Si el archivo cloudinary.py está en el mismo directorio que este archivo
from . import APIException  # Si el archivo APIException.py está en el mismo directorio que este archivo

from routes import api

cloudinary.config(
  cloud_name = "dztgp8g6w",
  api_key = "158344581497744",
  api_secret = "a5xb9RBMOpovJEOOranrRYLWAYw"
)

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