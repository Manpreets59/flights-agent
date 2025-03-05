from api_client import FlightAPI

flight_api = FlightAPI()
result = flight_api.get_flight_details("JFK")
print(result)