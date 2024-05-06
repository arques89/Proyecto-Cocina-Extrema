from flask import Flask
from models import db , User , Chef , Concursantes
from routes import api
from flask_cors import CORS
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from config import Config
from flask_jwt_extended import JWTManager

migrate = Migrate()

admin = Admin(name='Admin Panel', template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Chef, db.session))
admin.add_view(ModelView(Concursantes, db.session))
# admin.add_view(ModelView(Concursantes, db.session))

def create_app():
    
    # Crear una instancia de la aplicación Flask
    app = Flask(__name__)
    
    app.config["JWT_SECRET_KEY"] = "super-secret"
    jwt = JWTManager(app)
    # Cargar la configuración desde config.py
    app.config.from_object(Config)
    
    # Configurar CORS para permitir solicitudes desde http://localhost:5173
    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

    # Configurar la base de datos SQLAlchemy
    db.init_app(app)
    
    # Inicializar Flask-Migrate
    migrate.init_app(app, db)
    
    # Registrar las rutas en la aplicación
    app.register_blueprint(api)

    # Inicializar la interfaz de administración
    admin.init_app(app)

    return app

# Comprobación para ejecutar el servidor de desarrollo
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)