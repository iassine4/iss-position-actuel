import requests

from datetime import datetime, timezone


iss_position_url = "http://api.open-notify.org/iss-now.json"

response = requests.get(iss_position_url)

print(response.status_code)
print(response.headers["Content-Type"])
print(response.text)

data = response.json()
print(data)

iss_position = data["iss_position"]
latitude = iss_position["latitude"]
longitude = iss_position["longitude"]
timestamp = data["timestamp"]

date_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)

print("Latitude:", latitude)
print("Longitude:", longitude)
print("Timestamp:", timestamp)

print("Date/heure UTC :", date_time)

people_url = "http://api.open-notify.org/astros.json"

people_response = requests.get(people_url)

print(people_response.status_code)
people_data = people_response.json()

people = people_data["people"]

iss_crew = [person for person in people if person["craft"] == "ISS"]
iss_crew_count = len(iss_crew)

print("Nombre d'occupants dans l'ISS :", iss_crew_count)

for person in iss_crew:
    print(person["name"])