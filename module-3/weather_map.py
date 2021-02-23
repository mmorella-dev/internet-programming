import datetime
import json
import requests

user_id = ""  # SUBSTITUTE ID HERE
user_apiid = ""  # SUBSTITUTE VALUE HERE

zip_code = "30092"

# make request to OpenWeatherMap API
weather_res = requests.get("https://api.openweathermap.org/data/2.5/weather"
                           + f"?zip={zip_code}"
                           + f"&appid={user_apiid}"
                           + "&units=imperial").json()

# print results
print("ZIP code:            \t", zip_code)
print("Name:                \t", weather_res["name"])
print("Current temperature: \t", weather_res["main"]["temp"], "°F")
print("Atmospheric pressure:\t", weather_res["main"]["pressure"], "hPa")
print("Wind speed           \t", weather_res["wind"]["speed"], "mph")
print("Wind direction       \t",
      weather_res["wind"]["deg"], "° clockwise from north")
report_time = datetime.datetime.fromtimestamp(weather_res["dt"])
print("Time of report       \t", report_time.isoformat(sep=' '))
