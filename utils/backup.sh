#!/bin/bash

# set up ssh pubkey login for TARGET host
# note: this can be insecure if your device ever gets compromised
# crontab example:
# TARGET=user@foo.bar:backup/
# @daily ~/ruuvicollector/backup.sh >> ~/ruuvi_backup.log

if [ -z "${TARGET}" ]; then
  echo "Backup TARGET env unset"
  exit
fi

# work in ramdisk to reduce sd writes
cd /tmp && sudo rm -rf ruuvi_backup

# take backup of all data
influxd backup -portable ruuvi_backup

# recompress archives (>50% smaller with xz)
pushd ruuvi_backup
for arc_in in *gz
do
  gunzip $arc_in
  tarball=$(basename $arc_in .gz)
  nice xz $tarball
done
popd

# dump some sd and fs stats
sudo ~/sdmon/src/sdmon /dev/mmcblk0 >ruuvi_backup/sd.txt
cat /sys/fs/ext4/mmcblk0p2/lifetime_write_kbytes >ruuvi_backup/fs.txt

# rsync files to safety and remove backup
rsync -av --delete ruuvi_backup $TARGET
rm -rf ruuvi_backup
