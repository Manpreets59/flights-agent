import os
import requests
from dotenv import load_dotenv

class FlightAPI:
    BASE_URL = "https://aerodatabox.p.rapidapi.com"

    def __init__(self, api_key=None):
        load_dotenv()
        self.api_key = api_key or os.getenv("API_KEY")

        if not self.api_key:
            raise ValueError("API Key is missing! Set it in .env or pass it as an argument.")

        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
        }

    def get_flight_details(self, airport_code):
        """Fetches flight details for a given airport code (IATA)"""
        url = f"{self.BASE_URL}/flights/airports/iata/{airport_code}"

        querystring = {
            "offsetMinutes": "-120",
            "durationMinutes": "720",
            "withLeg": "true",
            "direction": "Both",
            "withCancelled": "true",
            "withCodeshared": "true",
            "withCargo": "true",
            "withPrivate": "true",
            "withLocation": "false"
        }

        try:
            response = requests.get(url, headers=self.headers, params=querystring)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {e}"}
