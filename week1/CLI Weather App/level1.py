import requests

cityName = input('Enter city name')
api_key = "755349663f5b82ad8bf6b90f0ed29a5c"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data['cod'] == 200:
    main = data["main"]
    weather = data["weather"]
    wind = data['wind']

    print("\n weather information")
    print(f"City: {cityName.title()}")
    print(f"Temperature: {main['temp']}c")
    print(f"weather: {weather['description'].title()}")
    print(f"")