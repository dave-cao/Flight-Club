import sys

import requests

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data = DataManager()
cities = data.get_cities()
flight_search = FlightSearch()


def populate_IATA():
    # Get city IATA code for each city gotten from google sheet
    for city in cities:
        city_code = flight_search.get_city_code(city)
        city["iataCode"] = city_code
        print(f"Retrieved {city_code} from {city['city']}")
    # Edit rows in google sheets
    data.update_cities(cities)


# Use flight search api to check for hte cheapest flights from tomorrow
# to 6 months laters for all the cities in the Google Sheet

# If the price is lower than the lowest price listed in the Google sheet
# then send an SMS to your own number with the Twilio API

for city in cities:
    cheapest = sys.maxsize
    cheapest_flight = None
    flight_data = FlightData(flight_search.get_flights(city["iataCode"]))
    cheapest_flight = flight_data.get_cheapest_flight()

    if cheapest_flight["price"] < city["lowestPrice"]:
        # send notification if cheap flight found
        notification_manager = NotificationManager(cheapest_flight)
        notification_manager.send_notification()
