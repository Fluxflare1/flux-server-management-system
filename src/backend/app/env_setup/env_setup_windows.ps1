# env_setup_windows.ps1

# Install Chocolatey (package manager for Windows)
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install Node.js
choco install nodejs -y

# Install Python
choco install python -y

# Verify installations
node --version
python --version

# Install pip dependencies if requirements.txt exists
if (Test-Path -Path "requirements.txt") {
    python -m pip install -r requirements.txt
}

# Install npm dependencies if package.json exists
if (Test-Path -Path "package.json") {
    npm install
}

Write-Output "Windows environment setup complete."
