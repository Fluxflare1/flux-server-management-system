#!/bin/bash

ENVIRONMENT=$(echo "$1" | tr '/' '_')

echo "Cleaning up environment: $ENVIRONMENT..."
docker-compose down
docker volume rm $(docker volume ls -q --filter "name=${ENVIRONMENT}")
