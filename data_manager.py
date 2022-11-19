import os

import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
        self.USER_ENDPOINT = os.environ["USER_ENDPOINT"]

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

    def post_users(self, first_name, last_name, email):
        """Post users into google sheet 'users'"""
        user_params = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        response = requests.post(url=self.USER_ENDPOINT, json=user_params)
        if response.ok:
            print("Your in the club!")
        else:
            print("Something went wrong here!")

    def get_users(self):
        response = requests.get(url=self.USER_ENDPOINT)
        return response.json()["users"]
