#!/bin/bash

# set up ssh pubkey login for target host
# note: this can be insecure if your device ever gets compromised
TARGET=user@foo.bar:backup/

# take backup of all data
influxd backup -portable ruuvi_backup

# recompress archives (>50% smaller with xz)
gunzip ruuvi_backup/*tar.gz
nice xz ruuvi_backup/*tar

# dump some sd and fs stats
sudo ~/sdmon/src/sdmon /dev/mmcblk0 >ruuvi_backup/sd.txt
sudo dumpe2fs /dev/mmcblk0p2|head -40 |grep -E "Free.blocks|Life" >ruuvi_backup/fs.txt

# rsync files to safety and remove backup
rsync -av --delete ruuvi_backup $TARGET
rm -rf ruuvi_backup
