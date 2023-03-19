import sqlite3
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 5

conn = sqlite3.connect('sensor_data.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS temperature_humidity_entries
                  (timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                   temperature REAL,
                   humidity REAL)''')

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        cursor.execute("INSERT INTO temperature_humidity_entries (temperature, humidity) VALUES (?, ?)", (temperature, humidity))
        conn.commit()

        print(f'Temperature: {temperature:.1f}C --- Humidity: {humidity:.1f}%')
    else:
        print('Failed to retrieve data from sensor')
    time.sleep(2)