#!/bin/bash

source config/environments/backup_config.env

TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
BACKUP_FILE="backup_$TIMESTAMP.tar.gz"
BACKUP_DIR="backups"

mkdir -p $BACKUP_DIR

# Create a compressed backup of the database and files
tar -czvf $BACKUP_DIR/$BACKUP_FILE src/backend/db src/uploads

if [[ "$BACKUP_PROVIDER" == "aws" ]]; then
    echo "Uploading backup to Amazon S3..."
    aws s3 cp $BACKUP_DIR/$BACKUP_FILE s3://$AWS_S3_BUCKET/
elif [[ "$BACKUP_PROVIDER" == "gcs" ]]; then
    echo "Uploading backup to Google Cloud Storage..."
    gcloud auth activate-service-account --key-file=$GCS_SERVICE_ACCOUNT_KEY
    gcloud storage cp $BACKUP_DIR/$BACKUP_FILE gs://$GCS_BUCKET/
elif [[ "$BACKUP_PROVIDER" == "local" ]]; then
    echo "Saving backup locally..."
    mv $BACKUP_DIR/$BACKUP_FILE $LOCAL_BACKUP_PATH/
else
    echo "No valid backup provider specified."
fi

# Cleanup old backups (keep only the last 7 backups)
find $BACKUP_DIR -type f -mtime +7 -exec rm {} \;

echo "Backup completed successfully!"
