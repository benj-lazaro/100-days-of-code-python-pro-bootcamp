import requests
import os
from twilio.rest import Client

# Constant Variable(s)
OWM_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LATITUDE = 14.599512
MY_LONGITUDE = 120.984222
MY_API_KEY = os.environ['OWM_API_KEY']
MY_PARAMETERS = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": MY_API_KEY,
    "exclude": "current,minutely,daily"
}

# Global Variable(s)
will_it_rain = False

# Access OpenWeatherMap (OWM) One Call API 1.0
response = requests.get(OWM_API_ENDPOINT, params=MY_PARAMETERS)
response.raise_for_status()

# Retrieve hourly data in JSON format
weather_data = response.json()

# Slice the weather data to get the 1st 12 hours [0 to 11]
weather_slice = weather_data["hourly"][:12]

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]

    # Check weather condition code; rain will likely occur if code < 700
    if int(condition_code) < 700:
        will_it_rain = True

if will_it_rain:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today! Remember to bring an umbrella.",
        from_="+15169089084",
        to="tee_hee_hee"
    )

    print(message.status)
