import requests
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta

# Constant Variable(s)
SHEETY_API_ENDPOINT = "https://api.sheety.co/9d844e80dc5b4da389794beb1cf9354b/flightDeals/prices"
POINT_OF_ORIGIN = "LON"

# Access the records (rows) from the registered spreadsheet (in Google Drive) using Sheety API
response = requests.get(url=SHEETY_API_ENDPOINT)
response.raise_for_status()
sheet_data = response.json()["prices"]

# Instantiate objects from classes
flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

# Search for the country's IATA code if the spreadsheet column is empty
if sheet_data[0]["iataCode"] == "":
    # Get the country's IATA code via Flight Search API
    for row in sheet_data:
        # row["iataCode"] = flight_search.get_destination_code(row["city"])
        row["iataCode"] = flight_search.find_iata_code(row["city"])

    # Pass updated sheet data to the DataManager class
    data_manager.destination_data = sheet_data
    # Call DAtaManager's method to update the corresponding destination codes
    data_manager.update_destination_code()

# Get tomorrow's date & time
tomorrow = datetime.now() + timedelta(days=1)
# Get date & time 5 months from today
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Check available flights based on the spreadsheet's IATA codes
for destination in sheet_data:
    flight = flight_search.check_flights(
        POINT_OF_ORIGIN,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # Access returned flight data's destination city & flight rate
    try:
        if flight.price < destination["lowestPrice"]:
            print("Accessing Twilio API")
            sms_message = "Low proce. Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} " \
                          "to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to " \
                          "{flight.return_date}."
            notification_manager.send_sms(message=sms_message)
    except AttributeError:
        pass
