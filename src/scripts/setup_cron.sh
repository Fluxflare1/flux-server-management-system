#!/bin/bash

source config/environments/backup_config.env

# Schedule the backup script using cron
(crontab -l 2>/dev/null; echo "$BACKUP_CRON_SCHEDULE bash $(pwd)/src/scripts/backup.sh") | crontab -

echo "Backup schedule configured successfully!"
