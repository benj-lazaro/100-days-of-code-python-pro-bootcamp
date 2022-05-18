import requests
import smtplib

# Constant Variable(s)
OWM_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LATITUDE = 14.599512
MY_LONGITUDE = 120.984222
MY_API_KEY = "qwertyuiop1234567890zxcvbnm,./"
MY_PARAMETERS = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": MY_API_KEY,
    "exclude": "current,minutely,daily"
}
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "test.dummy@gmail.com"
SENDER_EMAIL_PASSWORD = "expectingmypasswordaintya?"
RECIPIENT_EMAIL = "test.dummy@gmail.com"

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

# NOTE: Instead of using Twilio API (due to privacy concerns), switched to using SMTP instead
if will_it_rain:
    message = "It's going to rain today!\nRemember to bring an umbrella."

    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=f"Subject: Weather Update... \n\n{message}"
        )
