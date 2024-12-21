#!/bin/bash

BUCKET_NAME="flux-frontend-bucket"

# Build the front-end
npm install && npm run build

# Sync to S3 bucket
aws s3 sync build/ s3://$BUCKET_NAME --acl public-read
