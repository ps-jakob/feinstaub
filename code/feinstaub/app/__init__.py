import os
from flask import Flask
from flask_migrate import Migrate
from config import Config
from .database import db

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder=os.path.abspath("static"))
    app.config.from_object(Config)

    db.init_app(app) 
    Migrate(app, db)

    from app.routes import api
    app.register_blueprint(api, url_prefix='/api')

    from app.views import views
    app.register_blueprint(views)

    return app
