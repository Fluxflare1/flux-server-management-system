#!/bin/bash

BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)
if [[ "$BRANCH_NAME" == "main" ]]; then
  ENVIRONMENT="production"
elif [[ "$BRANCH_NAME" == "develop" ]]; then
  ENVIRONMENT="staging"
else
  ENVIRONMENT=$(echo "$BRANCH_NAME" | tr '/' '_')
fi

export ENVIRONMENT
echo "Environment configured: $ENVIRONMENT"
