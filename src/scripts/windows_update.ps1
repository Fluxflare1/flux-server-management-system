# PowerShell script for checking and installing updates
Install-Module PSWindowsUpdate -Force -Scope CurrentUser
Import-Module PSWindowsUpdate

# Check and install updates
Get-WindowsUpdate -AcceptAll -Install -AutoReboot
