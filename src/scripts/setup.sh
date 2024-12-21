

#!/bin/bash
echo "Initializing Database..."

if [ -z "$DATABASE_URL" ]; then
  echo "DATABASE_URL is not set. Exiting..."
  exit 1
fi

DB_HOST=$(echo $DATABASE_URL | cut -d'@' -f2 | cut -d':' -f1)
DB_PORT=$(echo $DATABASE_URL | cut -d':' -f3 | cut -d'/' -f1)
DB_NAME=$(echo $DATABASE_URL | cut -d'/' -f4)
DB_USER=$(echo $DATABASE_URL | cut -d':' -f2 | cut -d'/' -f3)
DB_PASS=$(echo $DATABASE_URL | cut -d':' -f2 | cut -d'@' -f1 | cut -d'/' -f3)

psql -h $DB_HOST -p $DB_PORT -U $DB_USER -c "CREATE DATABASE $DB_NAME;" || echo "Database already exists."

echo "Database initialized successfully!"




#!/bin/bash

echo "Setting up desktop shortcuts..."

if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    bash ./create_shortcut.sh
elif [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "cygwin"* ]]; then
    pwsh ./create_shortcut.ps1
else
    echo "Unsupported operating system."
fi




# Setup script for frontend dependencies
echo "Setting up frontend dependencies..."
cd ../frontend
yarn install
echo "Frontend dependencies installed successfully!"





#!/bin/bash

# Setup script for backend dependencies
echo "Setting up backend dependencies..."
cd ../backend
pip install -r requirements.txt
echo "Backend dependencies installed successfully!"




#!/bin/bash
# setup.sh

# Variables for shortcut creation
SERVER_MANAGER_DIR="$HOME/Desktop/FluxServerManager"
PROJECTS_DIR="$SERVER_MANAGER_DIR/Projects"

# Create directories if they don't exist
mkdir -p "$SERVER_MANAGER_DIR"
mkdir -p "$PROJECTS_DIR"

# Create server manager shortcut
ln -sf "$PWD/flux-server-management" "$SERVER_MANAGER_DIR/FluxServerManagerShortcut"

# Provide confirmation
echo "Server Manager and project folders shortcut created on Desktop."
