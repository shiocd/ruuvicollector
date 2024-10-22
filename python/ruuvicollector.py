from ruuvitag_sensor.ruuvi import RuuviTagSensor
from ruuvi_helpers import init_client, write_to_influxdb
from datetime import datetime
import yaml

client = init_client()

# load app configuration
with open("config.yml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

interval = cfg["interval"]
sensors = cfg["sensors"]

samples = {}
for key in sensors.keys():
    samples[key] = datetime.now()

def handle_rx(data):
    #print(f"{data[0]} {data[1]}")

    # received data mac
    mac = data[0]

    # only save rx samples every interval secs per mac
    cur_time = datetime.now()
    pre_time = samples[mac]
    if (cur_time-pre_time).total_seconds() > interval:
        write_to_influxdb(sensors, data, client)
        samples[mac] = datetime.now()
        #print("Write")
    else:
        pass
        #print("Skip")


if __name__ == "__main__":
    RuuviTagSensor.get_data(handle_rx, sensors.keys())

