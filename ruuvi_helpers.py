from influxdb import InfluxDBClient
from measurement_helpers import calc

def init_client():
    return InfluxDBClient(host="localhost", port=8086, database="ruuvi")

def write_to_influxdb(sensors, data, client):
    filter_mac = data[0]
    payload = data[1]
    name = sensors[filter_mac]
    mac = payload["mac"].upper()

    # calculated humidity, dew, vapor, density
    airdata = calc(payload["temperature"], payload["humidity"], payload["pressure"])

    dataFormat = payload["data_format"]

    fields = {}
    fields["absoluteHumidity"] = airdata["humidity"]
    fields["dewPoint"] = airdata["dew"]
    fields["equilibriumVaporPressure"] = airdata["vapor"]
    fields["airDensity"] = airdata["density"]

    fields["temperature"] = payload["temperature"]
    fields["humidity"] = payload["humidity"]
    fields["pressure"] = payload["pressure"]
    fields["batteryVoltage"] = payload["battery"] / 1000.0
    fields["movementCounter"] = payload["movement_counter"]
    fields["measurementSequenceNumber"] = payload["measurement_sequence_number"]
    fields["rssi"] = payload["rssi"]
    #fields["txPower"] = payload["tx_power"] if ("tx_power" in payload) else None
    #fields["tagID"] = payload["tagID"] if ("tagID" in payload) else None

    json_body = [
        {"measurement": "ruuvi_measurements", "tags": {"mac": mac, "name": name, "dataFormat": dataFormat}, "fields": fields}
    ]
    #print(json_body)
    client.write_points(json_body)
