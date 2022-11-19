# Flight Club

1. Google Sheets Data Management: https://sheety.co/
2. Kiwi Partners Flight Search API: https://partners.kiwi.com/
3. Twilio SMS API: https://www.twilio.com/docs/sms

Search through a list of cities from a google docs sheet. Each city row
contains a record low price. 

Search through all flights for each city from Edmonton --> City in google sheets
from tomorrow to the next 6 months. If there is a lower price then record low, 
then send me a text message!


## Usage

*Must have proper .env file for all API's*

1. run `python3 add_member.py` to add yourself to the flight club (stored in google sheet)
2. run `python3 main.py` to search a google sheet with my preferred travel destinations
and their historical low prices. If the program finds a flight price within 6 months
with a duration of 7-28 days (return flight) then it will email you from the email
you gave in `add_member.py`. 
3. Alternatively, if you are my friend, once you added yourself to the flight club,
the script will run daily on my server and automatically email you the flight deals!


