import requests

# Constant Variable(s)
OWM_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LATITUDE = 14.599512
MY_LONGITUDE = 120.984222
MY_API_KEY = "qwertyuiop1234567890zxcvbnm,./"
MY_PARAMETERS = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": MY_API_KEY
}

# Access OpenWeatherMap (OWM) One Call API 1.0
response = requests.get(OWM_API_ENDPOINT, params=MY_PARAMETERS)
response.raise_for_status()
# Retrieve response in JSON format
weather_data = response.json()
print(weather_data)
