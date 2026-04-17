import os
import requests
import sys


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = "Paris"

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        sys.exit(1)

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Current weather in {city}: {temp}°C, {condition}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
