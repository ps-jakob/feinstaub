import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder=os.path.abspath("static"))
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)
    Migrate(app, db)

    # Register API Blueprint (REST API)
    from app.routes import api
    app.register_blueprint(api, url_prefix='/api')

    # Register ViewController Blueprint (für HTML-Seiten)
    from app.views import views
    app.register_blueprint(views)  # Kein URL-Prefix, weil es HTML-Seiten sind

    return app
