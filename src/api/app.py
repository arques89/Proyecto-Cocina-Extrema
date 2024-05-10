import os
from flask import Flask

from flask_cors import CORS
from flask_migrate import Migrate
from config import Config
from flask_jwt_extended import JWTManager
from admin import admin
from mail import init_mail
from routes import api
from models import db

migrate = Migrate()

def create_app():
    # Crear una instancia de la aplicación Flask
    app = Flask(__name__)

    # Configurar la clave secreta JWT
    app.config["JWT_SECRET_KEY"] = os.environ.get('FLASK_APP_KEY')
    jwt = JWTManager(app)

    # Cargar la configuración desde config.py
    app.config.from_object(Config)

    # Configurar CORS para permitir solicitudes desde http://localhost:5173
    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

    # Configurar la base de datos SQLAlchemy
    db.init_app(app)

    # Inicializar Flask-Migrate
    migrate.init_app(app, db)

    # Inicializar Flask-Mail
    init_mail(app)

    # Registrar las rutas en la aplicación
    app.register_blueprint(api)

    # Inicializar la interfaz de administración
    admin.init_app(app)

    return app

# Comprobación para ejecutar el servidor de desarrollo
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
