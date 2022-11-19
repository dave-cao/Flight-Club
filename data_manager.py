import os

import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

    def get_cities(self):
        """Returns a list of city objects populated from the google sheets"""
        response = requests.get(url=self.SHEETY_ENDPOINT)
        return response.json()["prices"]

    def update_cities(self, cities):
        """Updates the google sheets with their new data
        Cities (list of dictionaries)"""
        for i, city in enumerate(cities):
            edit_sheety_endpoint = f"{self.SHEETY_ENDPOINT}/{i + 2}"
            edit_sheet_params = {"price": city}
            response = requests.put(url=edit_sheety_endpoint, json=edit_sheet_params)
            print(response, f"Edited row {i + 2}")
