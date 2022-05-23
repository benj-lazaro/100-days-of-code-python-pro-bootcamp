import requests

# Constant Variable(s)
SHEETY_API_ENDPOINT = "https://api.sheety.co/9d844e80dc5b4da389794beb1cf9354b/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __int__(self):
        self.destination_data = {}

    def update_destination_code(self):
        """Update a country's IATA code"""
        for city in self.destination_data:
            update_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{SHEETY_API_ENDPOINT}/{city['id']}", json=update_data)
            print(response.text)
