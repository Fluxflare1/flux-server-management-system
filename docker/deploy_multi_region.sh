#!/bin/bash

REGIONS=("us-east-1" "us-west-1" "eu-west-1")

for region in "${REGIONS[@]}"; do
  echo "Deploying to $region..."
  aws ecs create-service --cluster "${region}-cluster" \
    --service-name flux-backend \
    --task-definition flux-backend \
    --desired-count 2
done
