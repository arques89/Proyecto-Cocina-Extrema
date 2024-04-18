from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User

# No necesitas importar app desde .app, ya que se importará en app.py
# from .app import app

admin = Admin(name='Admin Panel', template_mode='bootstrap3')

def init_admin(app):
    admin.init_app(app)

    # Agrega vistas de modelos a la interfaz de administración
    admin.add_view(ModelView(User, db.session))

# Elimina el bloque "if __name__ == '__main__'" ya que no es necesario
