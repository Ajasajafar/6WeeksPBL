import requests

API_KEY = "755349663f5b82ad8bf6b90f0ed29a5c"
base_url = "http://api.openweathermap.org/data/2.5/weather"


def get_weather_data(city):
    '''Fetches weather data from OpenWeather API'''
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("⏳ Request timed out.")
        return None
    except requests.exceptions.ConnectionError:
        print("🔌 No internet connection.")
        return None
    except requests.exceptions.HTTPError:
        print("❗ Invalid API response or wrong city.")
        return None 
