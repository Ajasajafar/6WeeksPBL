from weather_utils import get_valid_city, extract_weather_details, display_weather, save_weather_file
from weather_api import get_weather_data

def main():
    print("🌦️ Welcome to the Level 2 Weather App!")

    while True:
        city = get_valid_city()
        if city is None:
            print("\nGoodbye! 👋")
            break

        data = get_weather_data(city)

        # If request failed (network or timeout)
        if data is None:
            continue

        # If API responded with invalid city
        if data.get("cod") != 200:
            print("❌ City not found. Try again.")
            continue

        weather = extract_weather_details(data)

        if weather:
            display_weather(weather)
        else:
            print("❗ Unexpected API format received.")
        save_weather_file(weather)
if __name__ == "__main__":
        main()    