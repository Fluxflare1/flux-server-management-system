#!/bin/bash

DATABASE_NAME="flux_db_${ENVIRONMENT}"

echo "Creating database for $ENVIRONMENT..."
psql -U $DATABASE_USER -c "CREATE DATABASE $DATABASE_NAME;"
