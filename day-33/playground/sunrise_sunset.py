import requests
from datetime import datetime

# Latitude & Longitude source: https://www.latlong.net/
MY_LATITUDE = 14.599512
MY_LONGITUDE = 120.984222

# API source: https://sunrise-sunset.org/api
response = requests.get(url="https://api.sunrise-sunset.org/json?lat=MY_LATITUDE&lng=MY_LONGITUDE&formatted=0")
response.raise_for_status()
data = response.json()

# Split the response data to get the hour (24-hour format)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")

time_now = datetime.now()
print(f"Current hour: {time_now.hour}")
