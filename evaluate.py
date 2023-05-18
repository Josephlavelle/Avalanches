from modules.Forecaster import Forecaster

print("Program Started")
testForecast = Forecaster((51.1784,-115.5708),["openWeatherMap","tomorrow.io"])
print("Forecaster Initialized")
testForecast.importForecastData(apiKeySource="apiKeys.txt")
print(testForecast.apiForecasts)