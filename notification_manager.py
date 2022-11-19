import os
from datetime import datetime

from twilio.rest import Client

TODAY = datetime.today().strftime("%Y-%m-%d")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight):
        self.flight = flight
        self.ACCOUNT_SID = os.environ["ACCOUNT_SID"]
        self.AUTH_TOKEN = os.environ["AUTH_TOKEN"]

    def send_notification(self):
        price = self.flight["price"]
        departure = self.flight["local_departure"].rsplit("T", 1)[0]
        IATA_from = self.flight["cityCodeFrom"]
        city_from = self.flight["cityFrom"]
        IATA_to = self.flight["cityCodeTo"]
        city_to = self.flight["cityTo"]

        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)
        message = client.messages.create(
            body=f"Low price alert! Only ${price} to fly from {city_from}-{IATA_from} to {city_to}-{IATA_to}, from {TODAY} to {departure}",
            from_=os.environ["TWILIO_NUMBER"],
            to=os.environ["MY_NUMBER"],
        )
        print(message.status)
