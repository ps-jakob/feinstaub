import requests
import os
import gzip
import shutil
from datetime import datetime, timedelta
import sys

def download_files(start_date, end_date, sensor_id, output_dir):
    base_url = "https://archive.sensor.community/2022/"
    file_format = "{date}/{date}_sds011_sensor_{sensor_id}.csv.gz"
    current_date = start_date
    delta = timedelta(days=1)

    os.makedirs(output_dir, exist_ok=True)  # Zielordner anlegen

    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        gz_filename = f"{date_str}_sds011_sensor_{sensor_id}.csv.gz"
        csv_filename = f"{date_str}_sds011_sensor_{sensor_id}.csv"

        file_link = base_url + file_format.format(date=date_str, sensor_id=sensor_id)
        gz_path = os.path.join(output_dir, gz_filename)
        csv_path = os.path.join(output_dir, csv_filename)

        print(f"Downloading {gz_filename}...")

        response = requests.get(file_link)
        if response.status_code == 200:
            with open(gz_path, 'wb') as f:
                f.write(response.content)

            print(f"{gz_filename} downloaded. Extracting...")

            # Entpacken
            with gzip.open(gz_path, 'rb') as f_in:
                with open(csv_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            os.remove(gz_path)  # .gz löschen
            print(f"{csv_filename} saved and {gz_filename} removed.")
        else:
            print(f"Failed to download {gz_filename}. Status code: {response.status_code}")

        current_date += delta

# Beispielaufruf
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
sensor_id = int(sys.argv[1])  # Sensor-ID über CLI
output_dir = "C:/Schule/SchuleDriveLink/Notizen/ITF24a/LF05/Projekte/Feinstaubsensor/datenTest"     # Zielverzeichnis

download_files(start_date, end_date, sensor_id, output_dir)
