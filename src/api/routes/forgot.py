from flask import request, jsonify, render_template
from models import db, User  # Importa el modelo de usuario y la instancia de base de datos
from flask_jwt_extended import create_access_token  # Para crear tokens de acceso
from flask_bcrypt import Bcrypt  # Para el hashing de contraseñas
from flask_mail import Message, Mail  # Para enviar correos electrónicos
from generate_password import *  # Si utilizas alguna función de generación de contraseñas
from routes import api

bcrypt = Bcrypt()  # Instancia de Bcrypt para el hashing de contraseñas
mail = Mail()  # Instancia de Mail para enviar correos electrónicos

@api.route('/forgot_password', methods=['POST'])
def forgot_password():
    
    user_check_email = request.json.get("email")
    print(user_check_email)
    user = User.query.filter_by(email=user_check_email).first()
    
    # Verificar si el usuario existe
    if not user:
        return jsonify({"error": "Usuario no existe"}), 404
    
    # Crear un mensaje de correo electrónico
    token = create_access_token(identity=str(user_check_email))

    # Almacenar el token en la base de datos para el usuario
    user.token = token
    db.session.commit()
    
    # Enviar el correo electrónico con el token
    send_password(user.email, user.name, token)
    
    return "Mensaje envido"

@api.route('/new_password/<token>', methods=['POST','GET'])
def new_password(token):
    user = User.query.filter_by(token=token).first()
    
    if not user:
        return jsonify({"error": "Token no válido"}), 404

    change_pass = gen_pass()
    hashed = bcrypt.generate_password_hash(change_pass)
    
    # Enviar la nueva contraseña al usuario
    sent_password(user.email, change_pass)
    
    user.password = hashed
    user.token = None
    db.session.commit()

    return render_template('new_password.html')

@api.route('/send_password')
def send_password(email, name, token):
    
    # Crear un mensaje de correo electrónico
    msg = Message('Restablecer tu Contraseña', 
    sender='arquesjavier@gmail.com', 
    recipients=[email])

    # Renderizar una plantilla HTML para el cuerpo del correo electrónico
    msg.html = render_template('forgot_password.html', 
    name=name, token=token)

    mail.send(msg)
    return jsonify({"message": "Correo electrónico enviado correctamente"}), 200

@api.route('/sent_password')
def sent_password(email, password_cambiada):
    
    # Crear un mensaje de correo electrónico
    msg = Message('Nueva contraseña', 
    sender='arquesjavier@gmail.com', 
    recipients=[email])
    msg.body = "Tu nueva contraseña es" + ' ' + password_cambiada
    # Renderizar una plantilla HTML para el cuerpo del correo electrónico

    mail.send(msg)
    return jsonify({"message": "Correo electrónico enviado correctamente"}), 200