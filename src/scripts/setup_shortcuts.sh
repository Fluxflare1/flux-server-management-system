#!/bin/bash

# setup_shortcuts.sh - Creates desktop shortcuts for project folder and dashboard

mkdir -p ~/Desktop/FluxServerManagement
ln -s "$(pwd)/flux-server-management/src/frontend/public" ~/Desktop/FluxServerManagement/Dashboard
ln -s "$(pwd)/flux-server-management/src/" ~/Desktop/FluxServerManagement/ProjectFolder

echo "Shortcuts created on desktop."
