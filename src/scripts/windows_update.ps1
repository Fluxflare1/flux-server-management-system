
# Load environment variables
$env:OS_UPDATE_ENABLED = $true
. ./config/environments/development.env

if ($env:AUTO_OS_UPDATE_ENABLED -eq "true") {
    Write-Output "Running Windows OS updates..."
    Invoke-Expression $env:WINDOWS_UPDATE_COMMAND
}



# PowerShell script for checking and installing updates
Install-Module PSWindowsUpdate -Force -Scope CurrentUser
Import-Module PSWindowsUpdate

# Check and install updates
Get-WindowsUpdate -AcceptAll -Install -AutoReboot
