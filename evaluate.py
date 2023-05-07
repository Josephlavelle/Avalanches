import requests as req
import pandas as pd
latitude, longitude = 51.46, -116.16
api = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"
response = req.get(f"{api}")
if response.status_code == 200:
    print("successfully fetched data")
    df = pd.DataFrame.from_dict(response.json())
    df.to_csv("testing/responseData.csv")
else:
    print("Error")
