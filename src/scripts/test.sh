#!/bin/bash

# Run backend tests
echo "Running backend tests..."
cd ../backend
python manage.py test

# Run frontend tests
echo "Running frontend tests..."
cd ../frontend
yarn test --watchAll=false
