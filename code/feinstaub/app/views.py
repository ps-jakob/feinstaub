from flask import Blueprint, render_template
from .models import Sensor
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/')
def index():
    start = datetime(2022, 1, 1).strftime("%Y-%m-%d")
    end = datetime(2022, 1, 10).strftime("%Y-%m-%d")
    return render_template(
        'index.html',
        startDate=start,
        endDate=end
                           )  # Lädt index.html aus dem templates-Ordner

## @views.route('/sensors')
## def show_sensors():
##     sensors = Sensor.query.all()  # Holt alle Sensoren aus der Datenbank
##     return render_template('sensors.html', sensors=sensors)
