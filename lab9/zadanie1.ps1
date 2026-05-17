<#
.SYNOPSIS
Pobiera aktualny średni kurs waluty do PLN wyświetla 5 ostatnich notowań wraz z datą

.DESCRIPTION
Skrypt korzysta z API NBP 

.PARAMETER curency_code
Wymaga podania 3 literowego kodu waluty

.EXAMPLE
.\zadanie1.ps1 USD

Kurs dolar amerykański
DATA -> ##### PLN
DATA -> ##### PLN
...

.NOTES
Autor Tobiasz Rolla
#>

#parametr skryptu kod waluty
param(
    [Parameter(Mandatory=$true)]
    [string] $currency_code
)

[string] $NBP_url = "https://api.nbp.pl/api/exchangerates/rates/a/$currency_code/last/5/?format=json"

$response = Invoke-RestMethod -Uri $NBP_url -Method GET

$currency = $response.currency

Write-Host "Waluta: $currency"

$response.rates | ForEach-Object {
    Write-Host "$($_.effectiveDate) -> $($_.mid) PLN"
}



