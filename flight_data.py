import sys


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight_data):
        self.flight_data = flight_data

    def get_cheapest_flight(self):
        cheapest = sys.maxsize
        cheapest_flight = {}
        for flight in self.flight_data:
            if cheapest > flight["price"]:
                cheapest = flight["price"]
                cheapest_flight = flight

        return cheapest_flight
