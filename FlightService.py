import requests
import datetime
import json
import os
from typing import List, Dict


class FlightService:
    def read_open_sky_api(self) -> List[Dict[str, str]]:
        url = "https://opensky-network.org/api/flights/departure"
        airport = "LFPG"  # ICAO code for Charles de Gaulle Airport
        date = "2022-12-01"
        start_time = int(datetime.datetime.strptime(date, "%Y-%m-%d").timestamp())
        end_time = start_time + 24 * 60 * 60

        params = {
            "airport": airport,
            "begin": start_time,
            "end": end_time
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            flight_data: List[Dict[str, str]] = []
            for flight in data:
                flight_dict = {
                    "icao24": flight["icao24"],
                    "firstSeen": flight["firstSeen"],
                    "estDepartureAirport": flight["estDepartureAirport"],
                    "lastSeen": flight["lastSeen"],
                    "estArrivalAirport": flight["estArrivalAirport"],
                    "callsign": flight["callsign"],
                    "estDepartureAirportHorizDistance": flight["estDepartureAirportHorizDistance"],
                    "estDepartureAirportVertDistance": flight["estDepartureAirportVertDistance"],
                    "estArrivalAirportHorizDistance": flight["estArrivalAirportHorizDistance"],
                    "estArrivalAirportVertDistance": flight["estArrivalAirportVertDistance"],
                    "departureAirportCandidatesCount": flight["departureAirportCandidatesCount"],
                    "arrivalAirportCandidatesCount": flight["arrivalAirportCandidatesCount"]
                }
                flight_data.append(flight_dict)
            return flight_data
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []

    def writing(self, flight: Dict[str, str]):
        flights_json = json.dumps(flight, default=lambda o: o.__dict__, indent=4)
        output_folder = "output"
        os.makedirs(output_folder, exist_ok=True)

        filename = "flights.json"
        output_path = os.path.join(output_folder, filename)
        with open(output_path, "w") as file:
            file.write(flights_json)
        print(f"Flights data written to {filename} successfully.")
