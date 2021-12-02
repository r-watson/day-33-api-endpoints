import requests
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

MY_LAT = 39.960339
MY_LONG = -76.734673
MY_ZONE = ZoneInfo("America/New_York")
str(MY_ZONE)

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# long = data["iss_position"]["longitude"]
# lat = data["iss_position"]["latitude"]
#
# iss_pos = (long, lat)
#
# print(iss_pos)

# Use request module raise_for_status() function instead of writing your own exceptions
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.")

paramters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=paramters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise, sunset)

time_now = datetime.now(tz=MY_ZONE)
print(time_now.hour)
