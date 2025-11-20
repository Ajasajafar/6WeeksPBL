from weather_utils import get_valid_city, extract_weather_details, display_weather, save_weather_file, get_sun_times, clear_screen
from weather_api import get_weather_data


def main():
    clear_screen()
    while True:
        print("🌦️ Welcome to the Level 3 Weather App!")
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
        sunrise, sunset = get_sun_times(data)
        if weather:
            display_weather(weather, sunrise, sunset)
        else:
            print("❗ Unexpected API format received.")
        save_weather_file(weather)
        choice = input("Check for another city? Y/N ")
        if choice.lower() == 'y':
             clear_screen()
             continue
        else:
             break
        
if __name__ == "__main__":
        main()    