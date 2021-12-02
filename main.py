import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

long = data["iss_position"]["longitude"]
lat = data["iss_position"]["latitude"]

iss_pos = (long, lat)

print(iss_pos)

# Use request module raise_for_status() function instead of writing your own exceptions
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.")