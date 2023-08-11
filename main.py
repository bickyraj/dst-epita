from DataModel.Flight import Flight
from typing import List
from FlightService import FlightService
from WeatherService import WeatherService


def main():
    flight_service = FlightService()
    flights: List[Flight] = flight_service.read_open_sky_api()
    for flight in flights:
        print(flight)
    # writing files to json
    flight_service.writing(flights)

    weather_service = WeatherService()
    weather_data = weather_service.read_weather("2023-07-06", "2023-07-12", "temperature_2m,relativehumidity_2m,windspeed_10m")
    print(weather_data)
    weather_service.write_weather(weather_data)

main()
