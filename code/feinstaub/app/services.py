from dataclasses import asdict

from flask import request

from dto.chart_dto import ChartDustEntry, ChartWeatherEntry
from .models import db, Sensor, DustMeasurement, WeatherMeasurement
from sqlalchemy import func, nullsfirst, text
from datetime import datetime, timedelta


def get_all_sensors():
    """Gibt alle Sensoren zurück."""
    return Sensor.query.all()

def get_sensor_by_name(sensor_name):
    """Sucht einen Sensor nach Name."""
    return Sensor.query.filter_by(sensor_name=sensor_name).first()


def get_selected_measurement(sensor_id, start_date, end_date):

    dates = generate_date_range(start_date, end_date)
    data = []

    print("Dates:")
    print(dates)

    if int(sensor_id) == 11496:
        print("ist in 11496")
        for date in dates:
            entry = ChartDustEntry(
                max_p1= get_max_p1(date),
                min_p1=get_min_p1(date),
                max_p2= get_max_p2(date),
                min_p2= get_min_p2(date),
                avg_p1= get_avg_p1(date),
                avg_p2= get_avg_p2(date),
            )
            data.append(asdict(entry))



    if int(sensor_id) == 113:
        print("ist in 113")
        for date in dates:
            entry = ChartWeatherEntry(
                min_temperature=get_min_temp(date),
                max_temperature=get_max_temp(date),
                avg_temperature=get_avg_temp(date),
                min_pressure=get_min_pressure(date),
                max_pressure=get_max_pressure(date),
                avg_pressure=get_avg_pressure(date),
                min_humidity=get_min_humidity(date),
                max_humidity=get_max_humidity(date),
                avg_humidity=get_avg_humidity(date),
                altitude=get_avg_altitude(date),
                min_pressure_sealevel=get_min_pressure_sealevel(date),
                max_pressure_sealevel=get_max_pressure_sealevel(date),
                avg_pressure_sealevel=get_avg_pressure_sealevel(date),
            )
            data.append(asdict(entry))

    return {
        "dates": dates,
        "measurements": data
    }





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
    sql = text("""
        SELECT MAX(p1) FROM dust_measurement
        WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_min_p1(timestamp):
    sql = text("""
    SELECT MIN(p1) FROM dust_measurement
    WHERE timestamp LIKE :ts
    """)

    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_avg_p1(timestamp):
    sql = text("""
    SELECT AVG(p1) FROM dust_measurement
    WHERE timestamp LIKE :ts
    """)

    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()


def get_max_p2(timestamp):
    sql = text("""
    SELECT MAX(p2) FROM dust_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()


def get_min_p2(timestamp):
    sql = text("""
    SELECT MIN(p2) FROM dust_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_avg_p2(timestamp):
    sql = text("""
    SELECT AVG(p2) FROM dust_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_min_temp(timestamp):
    sql = text("""
    SELECT MIN(temperature) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_max_temp(timestamp):
    sql = text("""
    SELECT MAX(temperature) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_avg_temp(timestamp):
    sql = text("""
    SELECT AVG(temperature) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_min_pressure(timestamp):
    sql = text("""
    SELECT MIN(pressure) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_max_pressure(timestamp):
    sql = text("""
    SELECT MAX(pressure) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_avg_pressure(timestamp):
    sql = text("""
    SELECT AVG(pressure) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_min_humidity(timestamp):
    sql = text("""
    SELECT MIN(humidity) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_max_humidity(timestamp):
    sql = text("""
    SELECT MAX(humidity) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_avg_humidity(timestamp):
    sql = text("""
    SELECT AVG(humidity) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_avg_altitude(timestamp):
    sql = text("""
    SELECT AVG(altitude) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()


def get_min_pressure_sealevel(timestamp):
    sql = text("""
    SELECT MIN(pressure_sealevel) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_max_pressure_sealevel(timestamp):
    sql = text("""
    SELECT MAX(pressure_sealevel) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

def get_avg_pressure_sealevel(timestamp):
    sql = text("""
    SELECT AVG(pressure_sealevel) FROM weather_measurement
    WHERE timestamp LIKE :ts
    """)
    like_pattern = f"{timestamp}%"
    result = db.session.execute(sql, {'ts': like_pattern})
    return result.scalar()

