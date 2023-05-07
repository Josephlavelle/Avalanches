import requests as req
latitude, longitude = 51.46, -116,16
api = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"
response = req.get(f"{api}")
if response.status_code == 200:
    print("successfully fetched data")
    print(response.json())
else:
    print("Error")
