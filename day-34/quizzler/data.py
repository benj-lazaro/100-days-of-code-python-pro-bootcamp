import requests

# Access the Open Trivia DB API & pass specific parameters
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()

# Access non-hardcoded questions
question_data = response.json()["results"]
