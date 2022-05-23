import requests
from flight_search import FlightSearch
from data_manager import DataManager

SHEETY_API_ENDPOINT = "https://api.sheety.co/9d844e80dc5b4da389794beb1cf9354b/flightDeals/prices"

# Access the records (rows) from the registered spreadsheet (in Google Drive) using Sheety API
response = requests.get(url=SHEETY_API_ENDPOINT)
response.raise_for_status()
sheet_data = response.json()["prices"]

# Search for the country's IATA code from the spreadsheet via Sheety API
if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    data_manager = DataManager()

    # Get the country IATA code via Tequila API
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    # Pass updated sheet data to the DataManager class
    data_manager.destination_data = sheet_data
    # Call DAtaManager's method to update the corresponding destination codes
    data_manager.update_destination_code()
