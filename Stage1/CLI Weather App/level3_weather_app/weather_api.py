import requests
from config import API_KEY,base_url

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
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        print("⏳ Request timed out.")
        return None
    except requests.exceptions.ConnectionError:
        print("🔌 No internet connection.")
        return None
    except requests.exceptions.HTTPError:
        print("❗ Invalid API response or wrong city.")
        return None 