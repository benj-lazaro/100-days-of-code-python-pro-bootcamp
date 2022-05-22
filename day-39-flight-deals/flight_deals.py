import requests
from flight_search import FlightSearch

SHEETY_API_ENDPOINT = "https://api.sheety.co/9d844e80dc5b4da389794beb1cf9354b/flightDeals/prices"
SHEETY_BEARER_TOKEN = "Bearer VGhpcyBpcyBhIHRlc3Qgb2YgdGhlIFBoaWxpcHBpbmUgQnJvYXNjYXN0IFN5c3RlbQ=="

response = requests.get(url=SHEETY_API_ENDPOINT)
response.raise_for_status()
sheet_data = response.json()["prices"]

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    print(f"{sheet_data}")
