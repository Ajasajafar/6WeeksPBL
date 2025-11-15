import requests

while True:
    cityName = input('Enter city name: ')
    api_key = "755349663f5b82ad8bf6b90f0ed29a5c"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
    except requests.exceptions.HTTPError as e:
        print("HTTP ERROR:", e)
    except requests.exceptions.RequestException as e:
        print("Network error:", e)

    if data['cod'] == 200:
        main = data["main"]
        weather = data["weather"]
        wind = data['wind']

        print("\n weather information".upper())
        print(f"City: {cityName.title()}")
        print(f"Temperature: {main['temp']}C")
        print(f"weather: {weather[0]['description']}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("\n City not found. Please check the name and try again.")