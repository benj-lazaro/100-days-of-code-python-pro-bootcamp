import requests
import os
from datetime import datetime

# Constant Variable(s)
NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_API_ID"]
NUTRITIONIX_API_KEY = os.environ["NUTRITIONIX_API_KEY"]

SHEETY_API_ENDPOINT = "https://api.sheety.co/9d844e80dc5b4da389794beb1cf9354b/workoutTracking/workouts"
SHEETY_BEARER_TOKEN = os.environ["SHEETY_BEARER_TOKEN"]

GENDER = os.environ["USER_GENDER"]
WEIGHT_KG = os.environ["USER_WEIGHT_KG"]
HEIGHT_CM = os.environ["USER_HEIGHT_CM"]
AGE = os.environ["USER_AGE"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Send POST request to Nutritionix API with input JSON data
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# Format current system date and time
today = datetime.now()
current_date = today.strftime("%d/%m/%Y")
current_time = today.strftime("%X")

# Comb through & format received JSON data from Nutritionix API
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
    }

    # Send a POST request to the Sheety API with Bearer Token authentication
    response = requests.post(url=SHEETY_API_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
    result = response.json()
