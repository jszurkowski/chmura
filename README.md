# Opis

Aplikacja wyświetla komunikat hello word dzięki Serverless - Azure Functions

## Wymagania

1. Ubuntu
2. Zainstalowane:
	* azure-cli
	* azure functionscore tool
	* python 3.X

## Uruchomienie lokalne

Pobierz repozytorium

```
git clone https://github.com/jszurkowski/chmura

```

Zainstaluj środowisko wirtualne

```python -m venv .venv
```

Uruchom środowisko wirtualne

```source .venv/bin/activate
```

Sprawdź czy masz zainstalowane Azure Function Core Tools

```func --version
```

Jeśli nie, to zainstaluj

```sudo apt-get install azure-functions-core-tools-4
```

Uruchom

``` func start

# w oknie przeglądarki wklej:
http://localhost:7071/api/HttpHello
```
## Uruchomienie w chmurze

Zaloguj się do Azure

```az login

az config param-persist on
```

Utwórz zasoby

```az group create --name <NAME> --location <REGION>

az storage account create --name <STORAGE_NAME> --sku Standard_LRS

az functionapp create --consumption-plan-location westeurope --runtime python --runtime-version 3.8 --functions-version 3 --name <APP_NAME> --os-type linux --storage-account <STORAGE_NAME>
```

Publikuj

```func azure functionapp publish <APP_NAME>
```

Sprawdź

```curl https://httphello.azurewebsites.net/api/httphello

Hello Word
Jakub Xxxxxxxxxx
nr albumu: 6XXX7
```

Na koniec wykasuj recource group

```az group delete --resource-group <NAZWA>
```
# chmura
