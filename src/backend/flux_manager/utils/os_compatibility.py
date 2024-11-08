# src/backend/flux_manager/utils/os_compatibility.py

import os
import platform

def create_desktop_shortcut(shortcut_name, target_path):
    if platform.system() == "Windows":
        create_windows_shortcut(shortcut_name, target_path)
    elif platform.system() == "Linux":
        create_linux_shortcut(shortcut_name, target_path)

def create_windows_shortcut(shortcut_name, target_path):
    # Windows shortcut creation logic
    print(f"Creating Windows shortcut for {shortcut_name} at {target_path}")

def create_linux_shortcut(shortcut_name, target_path):
    # Linux shortcut creation logic
    print(f"Creating Linux shortcut for {shortcut_name} at {target_path}")
