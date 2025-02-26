df = pd.read_csv(file_path, delimiter=";", dtype={
    "sensor_id": "Int64",  # Allows NaN values
    "sensor_type": str,
    "location": "Int64",
    "lat": "float64",
    "lon": "float64",
    "timestamp": str,
    "pressure": "float64",
    "altitude": "float64",
    "pressure_sealevel": "float64",
    "temperature": "float64",
    "humidity": "float64"
})

class Sensor:
    def __init__(self):