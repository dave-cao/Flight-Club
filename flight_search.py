import datetime
import os

import requests
from dateutil.relativedelta import relativedelta

TODAY = datetime.datetime.today()
TOMORROW = TODAY + datetime.timedelta(days=1)
SIX_MONTHS_LATER = TODAY + relativedelta(months=+6)
SEVEN_DAYS_LATER = TODAY + datetime.timedelta(days=7)
TWENTY_EIGHT_DAYS_LATER = TODAY + datetime.timedelta(days=28)


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.FLIGHT_API = os.environ["FLIGHT_API"]
        self.FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com"
        self.FLIGHT_HEADER = {
            "apikey": self.FLIGHT_API,
            "Content-Type": "application/json",
        }

    def get_city_code(self, city):
        """Returns the city code of arg city.
        city (str)"""
        location_endpoint = f"{self.FLIGHT_ENDPOINT}/locations/query"
        flight_params = {
            "term": city["city"],
            "location_types": "city",
            "locale": "en-US",
            "limit": 1,
        }

        response = requests.get(
            url=location_endpoint,
            headers=self.FLIGHT_HEADER,
            params=flight_params,
        )
        city_data = response.json()["locations"][0]
        return city_data["code"]

    def get_flights(self, fly_to):
        """Takes in where you want to fly and gets all the flights for that
        from tomorrow to the next 6 months. Returns flights as a list of objects
        fly_to (str): the IATA code of the city you want to go to."""
        search_endpoint = f"{self.FLIGHT_ENDPOINT}/v2/search"
        search_params = {
            "fly_from": "YEG",
            "fly_to": fly_to,
            "date_from": f"{TOMORROW.strftime('%d/%m/%Y')}",
            "date_to": f"{SIX_MONTHS_LATER.strftime('%d/%m/%Y')}",
            "curr": "CAD",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            # "price_to": "",
        }

        response = requests.get(
            url=search_endpoint, headers=self.FLIGHT_HEADER, params=search_params
        )
        print(f"Got flight data for YEG --> {fly_to}")
        return response.json()["data"]
