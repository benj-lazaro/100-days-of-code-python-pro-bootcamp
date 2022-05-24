import requests
import os
from flight_data import FlightData

# Constant Variable(s)
FLIGHT_SEARCH_API_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_KIWI_API_KEY = os.environ["TEQUILA_KIWI_API_KEY"]
CURRENCY = "GBP"


class FlightSearch:

    # def get_destination_code(self, city):
    #     """Fetches the destination code"""
    #     destination_code = "TESTING"
    #     return destination_code

    def find_iata_code(self, city):
        """Returns the corresponding IATA code of a city"""
        header = {
            "apikey": TEQUILA_KIWI_API_KEY,
        }
        search_data = {
            "term": city,
        }

        response = requests.get(url=f"{FLIGHT_SEARCH_API_ENDPOINT}/locations/query", params=search_data, headers=header)
        iata_code = response.json()["locations"][0]["code"]
        return iata_code

    def check_flights(self, origin_code, destination_code, from_time, to_time):
        headers = {
            "apikey": TEQUILA_KIWI_API_KEY
        }

        query = {
            "fly_from": origin_code,
            "fly_to": destination_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "to_time": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": CURRENCY,
        }

        response = requests.get(url=f"{FLIGHT_SEARCH_API_ENDPOINT}/v2/search", headers=headers, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No destination flights for {destination_code}")
            return None

        # Save returned data to FlightData class
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        # Print & return destination flight rate(s)
        print(f"Destination {flight_data.destination_city} = £{flight_data.price}")
        return flight_data
