from flask_mail import Mail
mail = Mail()
def init_mail(app):
    # Inicializar Flask-Mail con los parámetros de Mailtrap
    app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = '1881b7d6d77790'
    app.config['MAIL_PASSWORD'] = '570a5a17717f9d'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    mail.init_app(app)