import requests
from datetime import datetime
import os

# Constant Variable(s)
PIXELA_API_ENDPOINT = "https://pixe.la/v1/users"

USER_NAME = os.environ["PIXELA_USER_NAME"]
USER_TOKEN = os.environ["PIXELA_USER_API_TOKEN"]

PIXELA_HEADERS = {
    "X-USER-TOKEN": USER_TOKEN,
}

PIXELA_GRAPH_ID = "graph1"

PIXELA_CREATE_USER_PARAMETERS = {
    "token": USER_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

PIXELA_CREATE_GRAPH_ENDPOINT = f"{PIXELA_API_ENDPOINT}/{USER_NAME}/graphs"
PIXELA_CREATE_GRAPH_CONFIG = {
    "id": PIXELA_GRAPH_ID,
    "name": "Programming Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}

PIXELA_POST_PIXEL_ENDPOINT = f"{PIXELA_API_ENDPOINT}/{USER_NAME}/graphs/{PIXELA_GRAPH_ID}"

# Create a user account in Pixela (USE THIS CODE BLOCK ONCE)
# response = requests.post(url=PIXELA_API_ENDPOINT, json=PIXELA_CREATE_USER_PARAMETERS)
# print(response.text)

# Create a graph definition (USE THIS CODE BLOCK ONCE)
# response = requests.post(url=PIXELA_CREATE_GRAPH_ENDPOINT, json=PIXELA_CREATE_GRAPH_CONFIG, headers=PIXELA_HEADERS)
# print(response.text)

# *** NOTE: To view graph on the browser: https://pixe.la/v1/users/<user_name>/graphs/<graph_id>.html ***

# To get a date of a specified day
# specific_day = datetime(year=1998, month=9, day=1)

# Get current date in YYYYMMDD format (https://www.w3schools.com/python/python_datetime.asp)
today = datetime.now()
current_date = today.strftime("%Y%m%d")

# Prepare POST request body
post_a_pixel = {
    "date": current_date,
    "quantity": "1",
}

# To post a pixel in the graph
# response = requests.post(url=PIXELA_POST_PIXEL_ENDPOINT, json=post_a_pixel, headers=PIXELA_HEADERS)
# print(response.text)

# To update the quantity of an existing pixel
# target_date = current_date
# update_pixel_endpoint = f"{PIXELA_API_ENDPOINT}/{USER_NAME}/graphs/{PIXELA_GRAPH_ID}/{target_date}"
#
# update_pixel = {
#     "quantity": "5",
# }
#
# response = requests.put(url=update_pixel_endpoint, json=update_pixel, headers=PIXELA_HEADERS)
# print(response.text)

# To delete a pixel from the graph
target_date = current_date
delete_pixel_endpoint = f"{PIXELA_API_ENDPOINT}/{USER_NAME}/graphs/{PIXELA_GRAPH_ID}/{target_date}"

response = requests.delete(url=delete_pixel_endpoint, headers=PIXELA_HEADERS)
print(response.text)
