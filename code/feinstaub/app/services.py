from .models import db, Sensor, DustMeasurement, WeatherMeasurement
from sqlalchemy import func, nullsfirst
from datetime import datetime, timedelta


def get_all_sensors():
    """Gibt alle Sensoren zurück."""
    return Sensor.query.all()

def get_sensor_by_name(sensor_name):
    """Sucht einen Sensor nach Name."""
    return Sensor.query.filter_by(sensor_name=sensor_name).first()


def get_selected_measurement(sensor_id, start_date, end_date):

    dates = generate_date_range(start_date, end_date)
    data = {}
    if sensor_id == 11496:
        for date in dates:

            max_p1 = get_max_p1(date)
            min_p1 = get_min_p1(date)
            avg_p1 = get_avg_p1(date)
            max_p2 = get_max_p2(date)
            min_p2 = get_min_p2(date)
            avg_p2 = get_avg_p2(date)



def generate_date_range(start_date_str, end_date_str):
    start = datetime.strptime(start_date_str, "%Y-%m-%d")
    end = datetime.strptime(end_date_str, "%Y-%m-%d")

    if start > end:
        raise ValueError("Startdatum darf nicht nach dem Enddatum liegen.")

    date_list = []
    current = start
    while current <= end:
        date_list.append(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1)

    return date_list

def get_max_p1(timestamp):
    sql = """
        SELECT MAX(p1) FROM dust_measurement
        WHERE timestamp LIKE :ts
    """
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_min_p1(timestamp):
    sql = """
    SELECT MIN(p1) FROM dust_measurement
    WHERE timestamp LIKE :ts
    """

    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_avg_p1(timestamp):
    sql = """
    SELECT AVG(p1) FROM dust_measurement
    WHERE timestamp LIKE :ts
    """

    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()


def get_max_p2(timestamp):
    sql = """
    SELECT MAX(p2) FROM dust_measurement
    WHERE timestamp LIKE :ts
    """
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()


def get_min_p2(timestamp):
    sql = """
    SELECT MIN(p2) FROM dust_measurement
    WHERE timestamp LIKE :ts
    """
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_avg_p2(timestamp):
    sql = """
    SELECT AVG(p2) FROM dust_measurement
    WHERE timestamp LIKE :ts
    """
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_min_temp(timestamp):
    sql = """
    SELECT MIN(temperature) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_max_temp(timestamp):
    sql = """
    SELECT MAX(temperature) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_avg_temp(timestamp):
    sql = """
    SELECT AVG(temperature) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

