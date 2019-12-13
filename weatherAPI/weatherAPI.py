#! python3
#quickweather app, prints weather for a location from the command line
# Created by Mark Foos

import json, requests, sys, time, math

# Compute Location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location not found')
    sys.exit()

location = ' '.join(sys.argv[1:])

url = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = "(enter your API Key here"
# city_name = input("Enter City Name: ")
complete_url = url + "appid=" + api_key + "&q=" + location
response = requests.get(complete_url)
response.raise_for_status()

weatherData = json.loads(response.text)
print(weatherData)
def Fahr(K):
    f = (K - 273.15) * 9/5 + 32
    return round(f)
def loadingDots():
    for i in range(3):
        print("...")
        time.sleep(.3)

def degToCompass(num):
    val = int(num)
    arr = ["North", "NorthEast", "East", "SouthEast", "South", "SouthWest", "West", "NorthWest"]
    if 22.5 > val < 337.5:
        return arr[0]
    else:
        return arr[math.floor((val + 22.5) / 45)]

# test print statements for converting degrees to Cardinal Direction

# print(str(degToCompass(0)))
# print(str(degToCompass(25)))
# print(str(degToCompass(90)))
# print(str(degToCompass(115)))
# print(str(degToCompass(160)))
# print(str(degToCompass(247)))
# print(str(degToCompass(248)))
# print(str(degToCompass(337)))

def mps2mph(speed):
    speed = speed * 2.23694
    return round(speed)

x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    temp_high = y["temp_max"]
    temp_low = y["temp_min"]
    z = x["weather"]
    weather_description = z[0]["description"]
    v = x["name"]
    location_name = v[:]
    wind = x["wind"]
    wind_speed = wind["speed"]
    try:
        wind["deg"] != "404"
        wind_dir = wind["deg"]
    except:
        wind_dir = "No Wind Direction Data"
    fahr = (current_temperature - 273.15) * 9/5 + 32

    # print(str(current_temperature))
    # print(str(Fahr(current_temperature)))
    # print(str(weather_description))
    # print(str(location_name))
    # print(str(Fahr(temp_high)))
    # print(str(Fahr(temp_low)))

    #main print output statements
    print("--" * 50 + "\n\n")
    print("Gathering weather data for " + str(location_name) + "\n")
    loadingDots()
    print("The current temperature is " + str(Fahr(current_temperature)) + " degrees.")
    loadingDots()
    print("The high for today is " + str(Fahr(temp_high)) + " degrees.")
    loadingDots()
    print("The low for today is " + str(Fahr(temp_low)) + " degrees.")
    loadingDots()
    print("The weather can be described as: " + str(weather_description))
    print("With a wind speed of " + str(mps2mph(wind_speed)) + " MPH")
    print("Coming from the " + str(degToCompass(wind_dir)))
else:
    print("City not found")
