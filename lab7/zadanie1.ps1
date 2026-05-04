[string]$PATH = "./TXTfolder"

if (Test-Path -Path $PATH) {
    Write-Host "folder exist"
}else {
    Write-Host "folder dose not exist"
    New-Item -Path $PATH -ItemType Directory 
}
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.PATH = "."
$watcher.Filter = ".txt"
$watcher.EnableRaisingEvents = true


