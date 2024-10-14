#!/bin/bash

TARGET=user@foo.bar:backup/

influxd backup -portable ruuvi_backup
rsync -av --delete ruuvi_backup $TARGET && rm -rf ruuvi_backup

