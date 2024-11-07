


#!/bin/bash

# Load environment variables
source config/environments/development.env

if [ "$AUTO_OS_UPDATE_ENABLED" = "true" ]; then
    echo "Running Linux OS updates..."
    eval $LINUX_UPDATE_COMMAND
fi





#!/bin/bash
# Update and upgrade system packages

echo "Updating package list..."
sudo apt update -y

echo "Upgrading packages..."
sudo apt upgrade -y

# Optionally, autoremove unnecessary packages
sudo apt autoremove -y
