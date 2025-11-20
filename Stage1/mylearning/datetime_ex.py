# from datetime import datetime, timedelta


# now = datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# Formatting date and time 
# formatted = now.strftime("%H:%M:%S %p")
# print(formatted)
# print(now.strftime("%B %d, %Y"))

# parsing strings into datetime
# text = "2025-11-18 14:30"
# dt = datetime.strptime(text, "%Y-%m-%d %H:%M")
# print(dt)

# Using timestamps
# timestamp = 1723457892
# sunrise = datetime.fromtimestamp(timestamp)
# print(sunrise.strftime("%d/%m/%Y, %H:%M:%S"))

#Time differences with timedelta
# today = datetime.now()
# future = today + timedelta(days=3)
# print(future)

import os, time
os.system("cls")

def loading():
    print("\nFetching weather ", end="")
    for _ in range(5):
        print(".", end="")
        time.sleep(1)     
    print("\n")
loading()
