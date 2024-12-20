#!/bin/bash

APP_NAME="FluxServerManagement"
APP_PATH="/usr/local/bin/flux-server"
DESKTOP_FILE="$HOME/Desktop/${APP_NAME}.desktop"

echo "[Desktop Entry]" > $DESKTOP_FILE
echo "Version=1.0" >> $DESKTOP_FILE
echo "Type=Application" >> $DESKTOP_FILE
echo "Name=$APP_NAME" >> $DESKTOP_FILE
echo "Exec=$APP_PATH" >> $DESKTOP_FILE
echo "Icon=/usr/local/share/icons/flux-icon.png" >> $DESKTOP_FILE
echo "Terminal=false" >> $DESKTOP_FILE

chmod +x $DESKTOP_FILE
echo "Desktop shortcut created at $DESKTOP_FILE"
