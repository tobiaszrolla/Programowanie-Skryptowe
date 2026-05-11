param(
    [Parameter(Mandatory=$true)]
    [string] $curency_name
)


[string] NBP_url = "https://api.nbp.pl/api/exchangerates/rates/a/$curency_name/today/?format=json"



