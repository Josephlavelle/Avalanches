import pandas as pd
import requests as req
from .auth import getAuth
class Forecaster:
    def __init__(self, coords: tuple[float,float], apis: list[str]):
        self.lat, self.longi = coords[0], coords[1]
        self.apis = apis
        self.apiForecasts = pd.DataFrame(columns=["Time", "Temperature"])
    def importForecastData(self, 
                           timeframeHours: int, 
                           apiKeySource: str):
        latitude, longitude = self.lat, self.longi
        apiKeys = getAuth(apiKeySource)
        forecastData = []
        for api, apiKey in apiKeys.items():
            # Fetch weather forecast for the coordinates
            print(f"Attemping to GET {api} data")
            url = ""
            if api == "openWeatherMap":
                url = f"http://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={apiKey}&units=metric"
            elif api == "tomorrow.io":
                url = f"https://api.tomorrow.io/v4/timelines?location={latitude},{longitude}&fields=temperature&timesteps=1h&units=metric&apikey={apiKey}"
            else:
                print(f"{api} not configured")
                continue
            # Make API call
            response = req.get(url)
            if response.status_code == 200:
                forecastData.append(response.json())
            else:
                print(f"Failed to GET {api} data")

        # Create a DataFrame to store the forecasts
        df = pd.DataFrame(columns=["Time", "Temperature"])
        # Extract forecasts from each API response and add them to the DataFrame
        for hour in range(timeframeHours):
            forecast = {}

            for data in forecastData:
                if "list" in data:
                    # openWeatherMap
                    temperature = data["list"][hour]["main"]["temp"]
                    forecast["openWeatherMap"] = temperature
                elif "data" in data and "timelines" in data["data"]:
                    # tomorrow.io
                    temperature = data["data"]["timelines"][0]["intervals"][hour]["values"]["temperature"]
                    forecast["tomorrow.io"] = temperature

            # Add the forecast as a row to the DataFrame
            df = df._append({"Time": hour + 1, "Temperature": forecast}, ignore_index=True)
        self.apiForecasts = df