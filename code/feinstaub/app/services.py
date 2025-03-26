from .models import db, Sensor, DustMeasurement, WeatherMeasurement
from sqlalchemy import func

def get_all_sensors():
    """Gibt alle Sensoren zurück."""
    return Sensor.query.all()

def get_sensor_by_name(sensor_name):
    """Sucht einen Sensor nach Name."""
    return Sensor.query.filter_by(sensor_name=sensor_name).first()

def get_measurements_for_sensor(sensor_id, start_date, end_date):
    """Holt Messwerte für einen bestimmten Sensor und Zeitraum."""
    return WeatherMeasurement.query.filter(
        WeatherMeasurement.sensor_id == sensor_id,
        WeatherMeasurement.timestamp >= start_date,
        WeatherMeasurement.timestamp <= end_date
    ).all()

def get_avg_temperature(sensor_id, start_date, end_date):
    """Gibt die Durchschnittstemperatur für einen Sensor und Zeitraum zurück."""
    avg_temp = db.session.query(func.avg(WeatherMeasurement.temperature)).filter(
        WeatherMeasurement.sensor_id == sensor_id,
        WeatherMeasurement.timestamp >= start_date,
        WeatherMeasurement.timestamp <= end_date
    ).scalar()
    return avg_temp

def get_latest_dust_measurement(sensor_id):
    """Holt die neueste Staubmessung für einen Sensor."""
    return DustMeasurement.query.filter_by(sensor_id=sensor_id).order_by(DustMeasurement.timestamp.desc()).first()
