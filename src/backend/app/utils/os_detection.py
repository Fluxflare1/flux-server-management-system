import platform
from config.logging_config import log_error

def configure_for_os():
    os_type = platform.system().lower()
    if os_type == "linux":
        configure_linux()
    elif os_type == "windows":
        configure_windows()
    else:
        log_error("Unsupported OS type")

def configure_linux():
    # Linux-specific setup
    print("Configuring for Linux")

def configure_windows():
    # Windows-specific setup
    print("Configuring for Windows")
