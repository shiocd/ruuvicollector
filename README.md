# Ruuvitag data collector for raspberry pi
![image](https://github.com/user-attachments/assets/54e67ba7-aba9-4a5d-a217-329309b4ded9)

## Collected data
### Measured
 - Temparature
 - Pressure
 - Battery voltage
 - RSSI
 - Measurements per hour
 - Movement counter activity
### Calculated
 - Dew point
 - Absolute humidity
 - Relative humidity
 - Air density
 - Vapor pressure

## Requirements
 - HW: raspberry pi, almost any version, 3B/3B+ used for testing
 - OS: raspberry os (lite) "bookworm"
 - Networking: wifi or ethernet, with internet access
 - ssh or direct local access for installation

## Installation
 - clone the repo to target host: pi $ `git clone https://github.com/shiocd/ruuvicollector.git`
 - run make: pi ruuvicollector$ `make`

## Configuration
  - Edit your ruuvi tag mac-addresses and names into python/config.yml

## Post installation setup
 - login to grafana at http://rasp\_ip:3000 (admin/admin)
 - change admin password during first login
 - import dashboard json from grafana\_templates dir

## Usage
 - access the dashboard from anywhere via tor-browser
 - access the host over ssh via same onion address, remember to copy over your ssh pubkey into /home/pi/.ssh/authorized\_hosts

## Storage health
 - for monitoring sd card health, consider using https://github.com/Ognian/sdmon

## Full influxdb backup
 - check the backup script in utils and adapt to your needs

## Info about system components
| Component | Description |
| --- | --- |
| influxdb | data storage |
| bluez | low level bluetooth access |
| ruuvicollector | ruuvitag -> BLE -> influxdb data flow |
| grafana | data visualization |
| tor | secure remote access |

## Thanks & acknowledgements
 - https://github.com/Scrin/RuuviCollector
 - https://github.com/ttu/ruuvitag-sensor
 - https://markokuosmanen.fi/2019-04-15-rasperry-pi-ruuvitag-tricks/
 - https://github.com/Ognian/sdmon
