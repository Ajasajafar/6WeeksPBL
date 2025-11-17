def get_valid_city():
    '''Asks the user for a city and validates the input.'''
    while True:
        city = input("\nEnter a city name(or 'exit' to quit)").strip()

        #Exit Option
        if city.lower() == "exit":
            return None
        
        # Check for empty input
        if not city:
            print("❗ City name cannot be empty. Try again.")
            continue

        # Check for invalid characters (digits, symbols)
        if not city.replace(" ", "").replace("-", "").isalpha():
            print("❗ Invalid city name. Only letters, spaces, and hyphens allowed.")
            continue

        return city

def extract_weather_details(data):
    """Extracts and returns clean weather information."""
    try:
        weather = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "condition": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    except KeyError:
        return None
    
def display_weather(weather):
    """Prints a clean formatted weather report."""
    print("\n--- WEATHER REPORT ---")
    print(f"City: {weather['city']}")
    print(f"Temperature: {weather['temp']}°C")
    print(f"Condition: {weather['condition']}")
    print(f"Description: {weather['description']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} m/s")
