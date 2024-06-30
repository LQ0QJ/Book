#!/bin/bash

set -Eeuxo pipefail

# Run this script by running: docker exec -it aa-data-import--web /scripts/download_aac_zlib3_files.sh
# Download scripts are idempotent but will RESTART the download from scratch!

rm -rf /temp-dir/aac_zlib3_files
mkdir /temp-dir/aac_zlib3_files

cd /temp-dir/aac_zlib3_files

curl -C - -O https://annas-archive.gs/dyn/torrents/latest_aac_meta/zlib3_files.torrent

# Tried ctorrent and aria2, but webtorrent seems to work best overall.
webtorrent download zlib3_files.torrent
