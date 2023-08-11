from typing import List, Dict, Union
import requests
import json
import os

class WeatherService:

    def read_weather(self, start_date, end_date, weather_type) -> List[Dict[str, str]]:
        url = f"https://api.open-meteo.com/v1/" \
              f"forecast?" \
              f"latitude=48.8534&" \
              f"longitude=2.3488&" \
              f"current_weather=true&" \
              f"hourly={weather_type}&" \
              f"start_date={start_date}&" \
              f"end_date={end_date}"
        response = requests.get(url)
        if response.status_code == 200:
            weather = response.json()
            weather_dict = {
                    "latitude": weather["latitude"],
                    "longitude": weather["longitude"],
                    "generationtime_ms": weather["generationtime_ms"],
                    "utc_offset_seconds": weather["utc_offset_seconds"],
                    "timezone": weather["timezone"],
                    "timezone_abbreviation": weather["timezone_abbreviation"],
                    "elevation": weather["elevation"],
                    "temperature": weather["current_weather"]["temperature"],
                    "windspeed": weather["current_weather"]["windspeed"],
                    "winddirection": weather["current_weather"]["winddirection"],
                    "weathercode": weather["current_weather"]["weathercode"],
                    "is_day": weather["current_weather"]["is_day"],
                    "time": weather["current_weather"]["time"]
                }
            return weather_dict
        else:
            raise Exception("Error fetching weather data")

    def write_weather(self, weather_data):
        data_json = json.dumps(weather_data, default=lambda o: o.__dict__, indent=4)
        output_folder = "output"
        os.makedirs(output_folder, exist_ok=True)

        filename = "weather.json"
        output_path = os.path.join(output_folder, filename)
        with open(output_path, "w") as file:
            file.write(data_json)
        print(f"Weather data written to {filename} successfully.")

