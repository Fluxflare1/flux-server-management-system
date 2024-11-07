#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux Setup
    echo "Running Linux environment setup..."
    python3 src/backend/app/env_setup/detect_dependencies.py

elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows Setup
    echo "Running Windows environment setup..."
    powershell.exe -File src/backend/app/env_setup/env_setup_windows.ps1
else
    echo "OS not supported."
fi
