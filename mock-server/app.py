from prometheus_client import start_http_server, Gauge
import random
import time

temperature = Gauge('temperature', 'Temperature')
humidity = Gauge('humidity', 'Humidity')
pressure = Gauge('pressure', 'Pressure')

def get_sensor_data():
    sensor_data = {
        'temperature': random.randint(20, 30),
        'humidity': random.randint(10,15),
        'pressure': random.randint(1,10)
    }
    return sensor_data

def update_metrics(sensor_data):
    """Update the Prometheus metrics with the sensor data."""
    temperature.set(sensor_data.get('temperature', 0))
    humidity.set(sensor_data.get('humidity', 0))
    pressure.set(sensor_data.get('pressure', 0))

def main():
    start_http_server(8000)
    
    while True:
        sensor_data = get_sensor_data()
        # print(sensor_data)
        update_metrics(sensor_data)
        time.sleep(1)

if __name__ == '__main__':
    main()
