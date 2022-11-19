import sys


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight_data):
        self.flight_data = flight_data

        self.cheapest_flight = self.get_cheapest_flight()

    def get_cheapest_flight(self):
        cheapest = sys.maxsize
        cheapest_flight = {}
        for flight in self.flight_data:
            if cheapest > flight["price"]:
                cheapest = flight["price"]
                cheapest_flight = flight

        return cheapest_flight

    def get_stopovers(self):
        """Returns stopovers (int) and stop_over_cities (list) as a tuple"""
        main_city_from = self.cheapest_flight["cityFrom"]
        main_city_to = self.cheapest_flight["cityTo"]
        route = self.cheapest_flight["route"]
        stop_overs = len(route) - 2
        stop_over_cities = [
            stop["cityTo"]
            for stop in route
            if stop["cityTo"] != main_city_from and stop["cityTo"] != main_city_to
        ]

        return (stop_overs, ", ".join(stop_over_cities))

    def get_departure_and_return(self):
        """Returns the depature and return date of flight"""
        route = self.cheapest_flight["route"]

        departure = route[0]["local_departure"]
        return_date = route[len(route) - 1]["local_arrival"]
        return (departure.rsplit("T", 1)[0], return_date.rsplit("T", 1)[0])
