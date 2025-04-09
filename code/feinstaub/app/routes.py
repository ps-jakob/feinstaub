from flask import Blueprint, request, jsonify
import os
import pandas as pd
from .models import db, Location, Sensor, DustMeasurement, WeatherMeasurement
from .services import get_selected_measurement

api = Blueprint('api', __name__)

@api.route('/import-data', methods=['POST'])
def import_data():
    data_dir = request.json.get('data_dir')
    if not data_dir or not os.path.exists(data_dir):
        return jsonify({'error': 'Invalid directory'}), 400

    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)
        if '113' in file and file.endswith('.csv'):
            df = pd.read_csv(file_path, sep=';', encoding='utf-8')
            for _, row in df.iterrows():
                location = Location.query.filter_by(loc=row['location']).first()
                if not location:
                    location = Location(loc=row['location'], lat=row['lat'], lon=row['lon'])
                    db.session.add(location)
                    db.session.commit()

                sensor = Sensor.query.filter_by(sensor_name=row['sensor_id']).first()
                if not sensor:
                    sensor = Sensor(location_id=location.id, sensor_type=row['sensor_type'], sensor_name=row['sensor_id'])
                    db.session.add(sensor)
                    db.session.commit()

                measurement = WeatherMeasurement(
                    sensor_id=sensor.id,
                    timestamp=row['timestamp'],
                    pressure=row.get('pressure'),
                    temperature=row.get('temperature'),
                    humidity=row.get('humidity'),
                    altitude=row.get('altitude'),
                    pressure_sealevel=row.get('pressure_sealevel')
                )
                db.session.add(measurement)
            db.session.commit()
        elif '11496' in file and file.endswith('.csv'):
            df = pd.read_csv(file_path, sep=';', encoding='utf-8')
            for _, row in df.iterrows():
                location = Location.query.filter_by(loc=row['location']).first()
                if not location:
                    location = Location(loc=row['location'], lat=row['lat'], lon=row['lon'])
                    db.session.add(location)
                    db.session.commit()

                sensor = Sensor.query.filter_by(sensor_name=row['sensor_id']).first()
                if not sensor:
                    sensor = Sensor(location_id=location.id, sensor_type=row['sensor_type'], sensor_name=row['sensor_id'])
                    db.session.add(sensor)
                    db.session.commit()

                measurement = DustMeasurement(
                    sensor_id=sensor.id,
                    timestamp=row['timestamp'],
                    p1=row.get('P1'),
                    p2=row.get('P2')
                )
                db.session.add(measurement)
            db.session.commit()

    return jsonify({'message': 'Data import completed'}), 200

@api.route('/get-measurements', methods=['GET'])
def get_measurements_api():
    """API-Endpunkt für Messwerte basierend auf vonDatum, bisDatum und sensorId"""
    sensor_id = request.args.get("sensorId")
    start_date = request.args.get("vonDatum")
    end_date = request.args.get("bisDatum")

    print(start_date)

    if not sensor_id or not start_date or not end_date:
        return jsonify({"error": "Bitte vonDatum, bisDatum und sensorId angeben"}), 400



    measurements = get_selected_measurement(sensor_id, start_date, end_date)
    print(measurements)
    return jsonify(measurements)