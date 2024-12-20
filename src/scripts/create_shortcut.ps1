$TargetPath = "C:\Program Files\FluxServerManagement\flux-server.exe"
$ShortcutLocation = "$env:USERPROFILE\Desktop\FluxServerManagement.lnk"
$WScriptShell = New-Object -ComObject WScript.Shell
$Shortcut = $WScriptShell.CreateShortcut($ShortcutLocation)
$Shortcut.TargetPath = $TargetPath
$Shortcut.WorkingDirectory = "C:\Program Files\FluxServerManagement"
$Shortcut.IconLocation = "$TargetPath, 0"
$Shortcut.Save()
Write-Output "Desktop shortcut created at $ShortcutLocation"
