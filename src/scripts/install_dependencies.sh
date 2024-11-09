#!/bin/bash
# Script for installing dependencies automatically for Django project

echo "Installing Python dependencies..."
pip install -r requirements.txt

# Additional installation for Django Channels if needed
pip install channels

echo "Dependencies installed."
