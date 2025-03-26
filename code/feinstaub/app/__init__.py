from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from .database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database with the Flask app
    db.init_app(app)
    Migrate(app, db)

    # Register API routes
    from app.routes import api
    app.register_blueprint(api, url_prefix='/api')

    return app
