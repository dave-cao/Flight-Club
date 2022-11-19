import os
import smtplib
from datetime import datetime

from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight):
        self.flight = flight
        self.ACCOUNT_SID = os.environ["ACCOUNT_SID"]
        self.AUTH_TOKEN = os.environ["AUTH_TOKEN"]

        self.price = self.flight["price"]
        self.departure = self.flight["depart_return"][0]
        self.return_date = self.flight["depart_return"][1]
        self.IATA_from = self.flight["cityCodeFrom"]
        self.city_from = self.flight["cityFrom"]
        self.IATA_to = self.flight["cityCodeTo"]
        self.city_to = self.flight["cityTo"]
        self.stopover_number = self.flight["stopovers"][0]
        self.stopover_cities = self.flight["stopovers"][1]
        self.nights = self.flight["nightsInDest"]

        self.message = f"Low price alert! Only ${self.price} to fly from {self.city_from}-{self.IATA_from} to {self.city_to}-{self.IATA_to}, from {self.departure} to {self.return_date} ({self.nights} nights).\n\nFlight has {self.stopover_number} stop over(s), via {self.stopover_cities}."

    def send_text(self):
        """Send a text message via twilio api"""
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)

        message = client.messages.create(
            body=self.message,
            from_=os.environ["TWILIO_NUMBER"],
            to=os.environ["MY_NUMBER"],
        )
        print(message.status)

    def send_email(self, users):
        flight_link = f"https://www.google.com/travel/flights?q=Flights%20to%20{self.IATA_to}%20from%20{self.IATA_from}%20on%20{self.departure}%20through%20{self.return_date}"
        for user in users:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
                connection.login(
                    user=os.environ["MY_EMAIL"], password=os.environ["MY_PASSWORD"]
                )
                connection.sendmail(
                    from_addr=os.environ["MY_EMAIL"],
                    to_addrs=user["email"],
                    msg=f"Subject:New Low Price Flight!\n\n{self.message}\n{flight_link}".encode(
                        "utf-8"
                    ),
                )
            print(f"Sent email to {user['firstName']}")
