from flask import Flask
from routes import routes
from models import db

# No necesitas importar app y db desde api.app, ya que ya están definidos aquí
# from api.app import app, db

from admin import admin

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')  # Carga la configuración desde config.py

    # Registra las rutas
    app.register_blueprint(routes)

    # Inicializa la base de datos
    db.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()

    # Agrega la vista de la interfaz de administración a la aplicación Flask
    admin.init_app(app)

    app.run(debug=True)
