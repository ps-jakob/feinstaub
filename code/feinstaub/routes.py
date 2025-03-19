from flask import Blueprint, request, jsonify
from models import db, DustMeasurement

routes = Blueprint('routes', __name__)

@routes.route('/dust_measurements', methods=['POST'])
def add_dust_measurement():
    data = request.json
    new_measurement = DustMeasurement(
        sensor_id=data['sensor_id'],
        timestamp=data['timestamp'],
        p1=data.get('p1', None),
        p2=data.get('p2', None)
    )
    db.session.add(new_measurement)
    db.session.commit()
    return jsonify({"message": "Messung hinzugefügt!"}), 201

@routes.route('/dust_measurements', methods=['GET'])
def get_dust_measurements():
    measurements = DustMeasurement.query.all()
    return jsonify([
        {"id": m.id, "sensor_id": m.sensor_id, "timestamp": m.timestamp, "p1": m.p1, "p2": m.p2}
        for m in measurements
    ])
