import requests
import json

api_key = "755349663f5b82ad8bf6b90f0ed29a5c"
base_url = "http://api.openweathermap.org/data/2.5/weather"

def main():
    def get_weather(cityName, api_key):
        params = {
            "q": cityName,
            "appid" : api_key,
            "units" : "metric"
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

    def parse_weather(data):
        if data is None:
            return None
        if data.get("cod") != 200:
            return None
        try:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            wind = data["wind"]["speed"]

            return {
                "temp" : temp,
                "humidity" : humidity,
                "description" : description,
                "wind" : wind
            }
        except KeyError:
            return None
        
    def show_weather(cityName, info):
        print("\n=====WEATHER REPORT=====")
        print(f"City: {cityName.title()}")
        print(f"Temperature: {info["temp"]}°C")
        print(f"Humidity: {info["humidity"]}%")
        print(f"Desc: {info["description"]}")
        print(f"Wind: {info["wind"]} m/s")
        print("==========================")


        print("Welcome To Level 2 Weather App")

        while True:
            cityName = input("Enter city name ").strip()
            
            if cityName.lower() == "exit":
                print("Goodbye!")
                break

            data = get_weather(cityName, api_key)
            info = parse_weather(data)

            if info:
                show_weather(cityName, info )
            else:
                print("Could not fetch weather, Check city name or network.")

main()