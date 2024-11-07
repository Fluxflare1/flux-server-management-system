import os
import subprocess

def run_command(command):
    """Run a command on the server based on the OS."""
    if os.name == 'nt':  # Windows
        completed_process = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
    else:  # Linux/Unix
        completed_process = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if completed_process.returncode != 0:
        print(f"Error: {completed_process.stderr}")
    else:
        print(completed_process.stdout)

    return completed_process.returncode
