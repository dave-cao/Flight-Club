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


def check_cheapest_flights():
    for city in cities:
        flight_data = FlightData(flight_search.get_flights(city["iataCode"]))
        cheapest_flight = flight_data.get_cheapest_flight()
        cheapest_flight["stopovers"] = flight_data.get_stopovers()
        cheapest_flight["depart_return"] = flight_data.get_departure_and_return()

        if cheapest_flight["price"] < city["lowestPrice"]:
            notification_manager = NotificationManager(cheapest_flight)
            # notification_manager.send_text()
            # get user data and send them email if cheap flight found
            users = data.get_users()
            notification_manager.send_email(users)


check_cheapest_flights()
