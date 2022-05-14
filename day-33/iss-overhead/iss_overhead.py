import requests
import datetime as dt
import smtplib
import time

# Constant Variable(s)
MY_LATITUDE = 14.599512
MY_LONGITUDE = 120.984222

SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "dummy.account"
SENDER_EMAIL_PASSWORD = "password12345"
RECIPIENT_EMAIL = "dummy.account@gmail.com"


def is_iss_nearby():
    """Checks if the ISS is within your current location"""
    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
        return True
    else:
        return False


def is_night_time():
    """Check if it is nighttime at your current location"""
    time_response = requests.get(url="https://api.sunrise-sunset.org/json?lat=MY_LATITUDE&lng=MY_LONGITUDE&formatted=0")
    time_response.raise_for_status()
    time_data = time_response.json()

    # Get the current sunrise & sunset hour using the 24-hour format & then convert it to an integer (string by default)
    my_sunrise = int(time_data["results"]["sunrise"].split("T")[1].split(":")[0])
    my_sunset = int(time_data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get current time
    time_now = dt.datetime.now().hour

    # Check if it is nighttime
    if time_now >= my_sunset or time_now <= my_sunrise:
        return True
    else:
        return False


# Access the endpoint of the ISS Current Location API
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

# Get the latitude & longitude of the ISS & then convert it to a float (string by default)
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

while True:
    # Sleep for 60 seconds before running the code below
    time.sleep(60)
    # Check if the ISS is overhead at nighttime in your current location
    if is_iss_nearby() and is_night_time():
        message = "The ISS is above you in the sky!"

        with smtplib.SMTP(SMTP_SERVER) as connection:
            # Establish a TLS connection
            connection.starttls()
            # Login using user credentials
            connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_PASSWORD)
            # Compose birthday email to intended recipient
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECIPIENT_EMAIL,
                msg=f"Subject: Look Up\n\n{message}"
            )
