from flask import Flask
from config import Config
from models import db
from routes import routes  # Importiere Blueprint

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(routes)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Flask-Projekt mit SQLite läuft!"

if __name__ == '__main__':
    app.run(debug=True)
