from .database import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loc = db.Column(db.Integer, nullable=False, unique=True)
    lat = db.Column(db.Float, nullable=True)
    lon = db.Column(db.Float, nullable=True)

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    sensor_type = db.Column(db.String, nullable=False)
    sensor_name = db.Column(db.String, nullable=False, unique=True)

class DustMeasurement(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)
    timestamp = db.Column(db.String, nullable=False)
    p1 = db.Column(db.Float, nullable=True)
    p2 = db.Column(db.Float, nullable=True)

class WeatherMeasurement(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)
    timestamp = db.Column(db.String, nullable=False)
    pressure = db.Column(db.Float, nullable=True)
    temperature = db.Column(db.Float, nullable=True)
    humidity = db.Column(db.Float, nullable=True)
    altitude = db.Column(db.Float, nullable=True)
    pressure_sealevel = db.Column(db.Float, nullable=True)
