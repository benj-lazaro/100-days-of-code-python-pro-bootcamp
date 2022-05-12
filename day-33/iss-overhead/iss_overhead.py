import requests

# Access the endpoint of the ISS Current Location API
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Raise an exception if the returned status code != 200
response.raise_for_status()

# Get the JSON data
data = response.json()

# Extract the current longitude and latitude of the ISS
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

# Print the location
print(f"ISS Position: {iss_position}")
