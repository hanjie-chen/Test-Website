#!/bin/sh
set -e

echo "[$(/bin/date '+%Y-%m-%d %H:%M:%S')] [CRON] scheduled sync triggered"
exec /sbin/su-exec appuser /usr/local/bin/update-articles.sh
