# Ruuvitag data collector for raspberry pi

## Requirements
 - armv7 raspberry pi board, almost any version
 - raspberry os lite running on the board
 - working network, wifi or ethernet, with internet access
 - ssh or local access for installation

## Server components
 - influxdb (data storage)
 - grafana (data visualization)
 - ruuvicollector (ruuvitag -> BLE -> influxdb)
 - tor (secure remote access)

## Configuration
  - Edit your ruuvi tag mac-addresses and names into config.yml

## Installation
 - clone the repo to target host: pi $ `git clone https://github.com/shiocd/ruuvicollector.git`
 - run make: pi ruuvicollector$ `make`

## Post installation
 - login to grafana at http://<raspi ip>:3000 (admin/admin)
 - change admin password during first login
 - import dashboard json from grafana\_templates dir

## Usage
 - access the dashboard from anywhere via tor-browser
 - access the host over ssh via same onion address, remember to copy over your ssh pubkey into ~/.ssh/authorized\_hosts
