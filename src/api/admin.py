from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User, Chef, Concursantes
admin = Admin(name='Admin Panel', template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Chef, db.session))
admin.add_view(ModelView(Concursantes, db.session))


