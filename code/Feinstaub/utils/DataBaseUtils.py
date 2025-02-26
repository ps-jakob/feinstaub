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
    db_file = r"C:\Schule\SchuleDriveLink\Notizen\ITF24a\LF05\Projekte\Feinstaubsensor\Repo\database\Feinstaubsensor.db"  # SQLite database file
    input_folder = r"C:\Schule\SchuleDriveLink\Notizen\ITF24a\LF05\Projekte\Feinstaubsensor\Repo\data"  # CSV source folder

    # Connect to SQLite
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Ensure table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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

    # Loop through all CSV files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):  # Ensure we only process CSV files
            file_path = os.path.join(input_folder, file_name)  # Construct full file path

            print(f"Processing: {file_path}")

            try:
                # Read CSV file into Pandas DataFrame
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

                # Check if the file has data
                if df.empty:
                    print(f"⚠️ Warning: {file_name} is empty, skipping.")
                    continue

                # Ensure all column names are in lowercase to prevent case mismatch issues
                df.columns = [col.lower() for col in df.columns]

                # Print column names for debugging
                print(f"Columns in {file_name}: {df.columns.tolist()}")

                # Insert into database (APPEND mode)
                df.to_sql("sensor_data", conn, if_exists="append", index=False)
                conn.commit()  # Commit after each file

                print(f"✅ Successfully inserted {file_name} into database.")

            except Exception as e:
                print(f"❌ Error processing {file_name}: {e}")

    # Close database connection
    conn.close()
    print("✅ All CSV files have been processed and stored in the database!")

# Run the function
import_data_to_db()
#unpack_files()