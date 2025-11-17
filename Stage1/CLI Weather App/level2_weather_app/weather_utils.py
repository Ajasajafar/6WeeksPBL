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
    
def c_to_f(temp_c):
    return round((temp_c * 9/5) + 32, 2)

from datetime import datetime

def get_sun_times(data):
    global sunrise, sunset
    try:
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")
        return sunrise, sunset
    except KeyError:
        return "N/A", "N/A"
    
def get_weather_emoji(condition):
    """Return emoji based on main weather condition"""
    condition = condition.lower()
    if "cloud" in condition:
        return "☁️"
    elif "rain" in condition:
        return "🌧️"
    elif "clear" in condition:
        return "☀️"
    elif "snow" in condition:
        return "❄️"
    elif "storm" in condition or "thunder" in condition:
        return "⛈️"
    else:
        return "🌡️"


def display_weather(weather, sunrise="N/A", sunset="N/A"):
    """Prints a clean formatted weather report."""
    global temp_f
    temp_f = c_to_f(weather['temp'])
    emoji = get_weather_emoji(weather['condition'])

    print("\n--- WEATHER REPORT ---")
    print(f"City: {weather['city']} {emoji}")
    print(f"Temperature: {weather['temp']}°C / {temp_f}°F")
    print(f"Condition: {weather['condition']}")
    print(f"Description: {weather['description']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} m/s")
    print(f"Sunrise: {sunrise} | Sunset: {sunset}")


def save_weather_file(weather):
    with open('C:\\6weeksPBL\\Stage1\\CLI Weather App\\level2_weather_app\\weather_log.txt', 'a') as file:
        file.write(f"City: {weather['city']}")
        file.write(f"\nHumidity: {weather['humidity']}%")  
        file.write(f"\nTemperature: {weather['temp']}°C / {temp_f}°F")    
        file.write(f"\nCondition: {weather['condition']}")    
        file.write(f"\nDescription: {weather['description']}")    
        file.write(f"\nWind Speed: {weather['wind_speed']} m/s\n\n\n")
        file.write(f"Sunrise: {sunrise} | Sunset: {sunset}")     
