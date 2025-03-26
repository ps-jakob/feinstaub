from flask import Blueprint, render_template
from .models import Sensor

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')  # Lädt index.html aus dem templates-Ordner

## @views.route('/sensors')
## def show_sensors():
##     sensors = Sensor.query.all()  # Holt alle Sensoren aus der Datenbank
##     return render_template('sensors.html', sensors=sensors)
