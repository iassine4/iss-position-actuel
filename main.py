import requests


iss_position_url = "http://api.open-notify.org/iss-now.json"

response = requests.get(iss_position_url)

print(response.status_code)
print(response.headers["Content-Type"])
print(response.text)

data = response.json()
print(data)

iss_position = data["iss_position"]