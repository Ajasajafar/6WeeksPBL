import json
import requests

response = requests.get()
data = response.json()

latitude = data["coord"]["lat"]
condition = data['weather'][0]["main"]
description =  data['weather'][0]["description"]
speed = data["wind"]["speed"]