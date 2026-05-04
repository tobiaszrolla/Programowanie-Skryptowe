
param(
    [Parameter(Mandatory=$true)]
    [string] $file_path,

    [Parameter(Mandatory=$true)]
    [string] $API_key
)

$MIN_MALICIOUS_LEVEL = 0
$MIN_SUSPICIOUS_LEVEL = 0

$file_hash = (Get-FileHash -Path $file_path -Algorithm SHA256).Hash

$headers = @{
    "accept"   = "application/json"
    "x-apikey" = $API_key
}

$url = "https://www.virustotal.com/api/v3/files/$file_hash"

$response = Invoke-RestMethod -Uri $url -Method GET -Headers $headers

$security_score = $response.data.attributes.last_analysis_stats

if($security_score.malicious -gt $MIN_MALICIOUS_LEVEL -or $security_score.suspicious -gt $MIN_SUSPICIOUS_LEVEL) {
    Write-Host "Plik nie jest bezpieczny!!!"

}else {
    Write-Host "Plik przeszedł bierzący test bezpieczeństwa"
}
