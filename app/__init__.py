import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fastag_parking.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Logging setup
    if not os.path.exists('app/logs'):
        os.makedirs('app/logs')
    file_handler = RotatingFileHandler('app/logs/fastag.log', maxBytes=10240, backupCount=5)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('FASTag Parking startup')

    db.init_app(app)

    # Create DB if not exists
    with app.app_context():
        from . import models
        db.create_all()

    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from . import forms

    return app 