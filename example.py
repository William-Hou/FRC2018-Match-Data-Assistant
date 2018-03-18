import requests
import json

parameters = {"lat": 44.05, "lon": -123.02}

response = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)
response2 = requests.get("http://api.open-notify.org/astros.json")

data = response2.json()
# print(data)


for item in data["people"]:
    print("Name: " + item["name"] + " Craft: " + item["craft"])


# print(response.content)
