from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Changer pour PostgreSQL  
from os import path
from flask_login import LoginManager 
from postgre import engine, Session
import os
import socket

database = os.environ.get('POSTGRES_DB')
username= os.environ.get('POSTGRES_USER')
pwd = os.environ.get('POSTGRES_PASSWORD')
port_id = 5432

postgres_host = 'postgres'
ip_address = socket.gethostbyname(postgres_host)

db = SQLAlchemy()


locale_session = Session(bind=engine)
url= f'postgresql://{username}:{pwd}@{ip_address}:{port_id}/{database}'

def create_app():
    app = Flask(__name__) # App initialization
    app.config['SECRET_KEY'] = 'secretkey' # Encrypt or secure the cookies and session data related to the website (DON'T STORE IT IN PLAIN TEXT)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{url}'
    db.init_app(app) #initialize database with the flask app



    from .views import views # import the Blueprint
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        db.create_all()
    

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #Where should flash redirect if user is not logged in and login is required
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))

    return app

