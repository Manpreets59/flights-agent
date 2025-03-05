import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class FlightAPI:
    BASE_URL = "https://aerodatabox.p.rapidapi.com"

    def __init__(self):
        self.api_key = os.getenv("RAPIDAPI_KEY")  # Load API key from .env
        if not self.api_key:
            raise ValueError("API Key not found! Make sure .env is set correctly.")
        
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
        
        response = requests.get(url, headers=self.headers, params=querystring)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Request failed: {response.status_code} {response.reason}"}
