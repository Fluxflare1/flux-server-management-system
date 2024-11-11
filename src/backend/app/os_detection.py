import platform

def detect_os():
    """Detects the OS of the current environment."""
    os_type = platform.system().lower()
    if os_type == 'linux':
        return 'linux'
    elif os_type == 'windows':
        return 'windows'
    else:
        return 'unknown'

def configure_server_os(os_type):
    """Configure server settings based on OS."""
    if os_type == 'linux':
        # Linux-specific configurations
        return linux_configuration()
    elif os_type == 'windows':
        # Windows-specific configurations
        return windows_configuration()
    else:
        raise ValueError("Unsupported OS type")

def linux_configuration():
    """Configurations specific to Linux servers."""
    return {
        "firewall": "iptables",
        "services": ["nginx", "mysql"],
        "permissions": "chmod 755"
    }

def windows_configuration():
    """Configurations specific to Windows servers."""
    return {
        "firewall": "Windows Defender",
        "services": ["IIS", "SQL Server"],
        "permissions": "icacls"
    }
