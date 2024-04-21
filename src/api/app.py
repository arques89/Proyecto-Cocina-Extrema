from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from admin import admin
from flask_cors import CORS
from routes import routes
from models import db, User, Chef

import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( 
    cloud_name = "dztgp8g6w", 
    api_key = "158344581497744", 
    api_secret = "a5xb9RBMOpovJEOOranrRYLWAYw" 
)

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Configurar CORS para permitir solicitudes desde http://localhost:5173
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Cargar la configuración desde config.py
app.config.from_pyfile('config.py')

# Configurar la base de datos SQLAlchemy
db.init_app(app)

# Inicializar Flask-Migrate
migrate = Migrate(app, db)

# Registrar las rutas en la aplicación
app.register_blueprint(routes)

# Inicializar la interfaz de administración
admin.init_app(app)

# Comprobación para ejecutar el servidor de desarrollo
if __name__ == "__main__":
    app.run(debug=True)
