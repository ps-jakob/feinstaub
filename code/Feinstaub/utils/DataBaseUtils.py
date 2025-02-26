import os
import gzip
import sqlite3
import shutil
import csv
import pandas as pd

def unpack_files():
    input_folder = r"C:\Schule\SchuleDriveLink\Notizen\ITF24a\LF05\Projekte\Feinstaubsensor\Daten"
    output_folder = r"C:\Schule\SchuleDriveLink\Notizen\ITF24a\LF05\Projekte\Feinstaubsensor\Repo\data"
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv.gz"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name[:-3])  # ".gz" entfernen

            # Datei entpacken
            with gzip.open(input_path, "rb") as f_in:
                with open(output_path, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)

            print(f"Entpackt: {file_name} → {output_path}")
        else:
            print("Error, Folder not found")

def import_data_to_db():
    db_file = "sensor_data.db"
    conn = sqlite3.connect('Feinstaubsensor.db')
    cursor = conn.cursor()

    input_folder = r"C:\Schule\SchuleDriveLink\Notizen\ITF24a\LF05\Projekte\Feinstaubsensor\Repo\data"
    output_folder = r"C:\Schule\SchuleDriveLink\Notizen\ITF24a\LF05\Projekte\Feinstaubsensor\Repo\database"

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY,
            sensor_id INTEGER,
            sensor_type TEXT,
            location INTEGER,
            lat REAL,
            lon REAL,
            timestamp TEXT,
            pressure REAL,
            altitude REAL,
            pressure_sealevel REAL,
            temperature REAL,
            humidity REAL
        )
    ''')

    for csv_file in os.listdir(input_folder):

        df = pd.read_csv(csv_file, delimiter=";", dtype={
            "sensor_id": int,
            "sensor_type": str,
            "location": int,
            "lat": float,
            "lon": float,
            "timestamp": str,
            "pressure": float,
            "altitude": float,
            "pressure_sealevel": float,
            "temperature": float,
            "humidity": float
        })

        df.to_sql("sensor_data", conn, if_exists="replace", index=False)