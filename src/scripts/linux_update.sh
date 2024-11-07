#!/bin/bash
# Update and upgrade system packages

echo "Updating package list..."
sudo apt update -y

echo "Upgrading packages..."
sudo apt upgrade -y

# Optionally, autoremove unnecessary packages
sudo apt autoremove -y
