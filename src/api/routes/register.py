from flask import request, jsonify, render_template
from models import db, User  # Importa el modelo de usuario y la instancia de base de datos
from flask_jwt_extended import create_access_token  # Para crear tokens de acceso
from flask_bcrypt import Bcrypt  # Para el hashing de contraseñas
from flask_mail import Message, Mail  # Para enviar correos electrónicos
from generate_password import *  # Si utilizas alguna función de generación de contraseñas
from flask_jwt_extended import create_access_token
from routes import api

bcrypt = Bcrypt()  # Instancia de Bcrypt para el hashing de contraseñas
mail = Mail()  # Instancia de Mail para enviar correos electrónicos

@api.route('/register', methods=['POST'])
def register_user():
    email = request.json["email"]
    password = request.json["password"]
    body = request.json

    user_exists = User.query.filter_by(email=email).first() is not None
    
    if user_exists:
        return jsonify({"error" : "User already exists"}), 409
    
    hashed_password = bcrypt.generate_password_hash(password)
    # Genera el token después de la creación del usuario
    token = create_access_token(identity=str(email))  # Suponiendo que la generación del token sea exitosa
    
    # Llamada a create_token pasando el correo electrónico
    new_user = User(email=email , password=hashed_password , name=body['name'], surname=body['surname'], token=token, is_active=False, is_admin=False)
    db.session.add(new_user)
    db.session.commit()
    
    confirm_account(email, new_user.name, token)
    # activate(token)
    return jsonify({
        "id" : new_user.id,
        "email" : new_user.email,
        'name': new_user.name,
        'surname': new_user.surname,
        'token': token  # Agregar el token a la respuesta JSON
    })
    
@api.route('/confirm_account')
def confirm_account(email, name, token):
    # Crear un mensaje de correo electrónico
    msg = Message('Confirma tu Cuenta', 
    sender='arquesjavier@gmail.com', 
    recipients=[email])

    # Renderizar una plantilla HTML para el cuerpo del correo electrónico
    msg.html = render_template('confirm_account.html', 
    name=name, email=email, token=token)
    # msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works."

    # Enviar el correo electrónico
    mail.send(msg)
    return 'Correo electrónico enviado correctamente!'

@api.route('/confirm_account/<token>')
def activate_account(token):
    # Fetch the user and validate the token
    user = User.query.filter_by(token=token).first()
    
    if not user:
        return jsonify({"error": "User not found or invalid token"}), 404
    elif user.token != token:
        return jsonify({"error": "Invalid token for user"}), 400

    # Activate the user account
    user.is_active = True
    user.token = None  # Optional: Remove the token after activation

    # Save changes to the database
    db.session.commit()

    # Send confirmation email (optional)
    confirm_account(email=user.email, name=user.name, token=token)
        # Redirect to login page
    return render_template('active_account.html', name=user.name,)

@api.route('/activate/<token>')
def activate(token):
    # Buscar al usuario por su dirección de correo electrónico
    # user = User.query.filter_by(email=email).first()
    user = User.query.filter_by(token=token).first()
    
    # Verificar si el usuario existe
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Verificar si el usuario ya está activo
    if user.is_active:
        return jsonify({"error": "User is already active"}), 400

    # Activar la cuenta del usuario
    user.is_active = True
    user.token = None  # Asegúrate de asignar None, no null

    # Guardar los cambios en la base de datos
    db.session.commit()

    return render_template('active_account.html')