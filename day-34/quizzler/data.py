import requests

# Parameters for the API
parameters = {
    "amount": 10,
    "type": "boolean",
}

# Access the Open Trivia DB API & pass specific parameters
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

# Get the questions from the received response
question_data = response.json()["results"]
