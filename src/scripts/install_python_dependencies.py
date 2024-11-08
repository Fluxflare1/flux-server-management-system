import subprocess

def install_dependencies():
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("Python dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error installing dependencies:", e)

install_dependencies()
