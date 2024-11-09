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
