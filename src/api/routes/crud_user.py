from flask import request, jsonify  # Para manejar las solicitudes HTTP y las respuestas JSON
from models import db, User  # Para acceder al modelo de datos de usuario y la instancia de base de datos

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