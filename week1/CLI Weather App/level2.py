import requests
import json

api_key = "755349663f5b82ad8bf6b90f0ed29a5c"
base_url = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(cityName, api_key):
    params = {
        'q': cityName,
        'appid' : api_key,
        'units' : 'metric'
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        data = response.json()
    except requests.exceptions.Timeout:
        return {"error": "Request timed out. Please check your connection"}
    except requests.exceptions.ConnectionError:
        return {"error": "Network error. Check your internet connection."}
    except Exception as e:
        return {"error": f"Unexpected error occurred: {e}"}
    return data