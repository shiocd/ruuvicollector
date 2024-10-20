#!/bin/bash

# set up ssh pubkey login for TARGET host
# note: this can be insecure if your device ever gets compromised
# crontab example:
# @daily TARGET=user@foo.bar:backup/ ~/backup.sh >> backup.log

if [ -z "${TARGET}" ]; then
  echo "Backup TARGET env unset"
  exit
fi

# take backup of all data
influxd backup -portable ruuvi_backup

# recompress archives (>50% smaller with xz)
gunzip ruuvi_backup/*tar.gz
nice xz ruuvi_backup/*tar

# dump some sd and fs stats
sudo ~/sdmon/src/sdmon /dev/mmcblk0 >ruuvi_backup/sd.txt
cat /sys/fs/ext4/mmcblk0p2/lifetime_write_kbytes >ruuvi_backup/fs.txt

# rsync files to safety and remove backup
rsync -av --delete ruuvi_backup $TARGET
rm -rf ruuvi_backup
