#Dodanie ścierzki jako stałej sprawdzenie i tworzenie folderu jeśli nie istnieje
[string]$PATH = "./TXTfolder"

if (Test-Path -Path $PATH) {
    Write-Host "folder exist"
}else {
    Write-Host "folder dose not exist"
    New-Item -Path $PATH -ItemType Directory 
}

#Inicjalizacja Watchera z filtrem plików txt i ścierzką 
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = "."
$watcher.Filter = "*.txt"
$watcher.EnableRaisingEvents = true

# nieskończona pętla czeka aż plik zostanie stworzony jak zostanie przenosi go
while ($true) {
    $change = $watcher.WaitForChanged("Created")
    Write-Host "Wykryto plik: $($change.Name)"
    
    Start-Sleep -Milliseconds 500 #krótka przerwa aby plik był załadowany do kopiowania
    Move-Item -Path $change.Name -Destination $PATH
}