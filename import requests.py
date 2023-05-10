import requests
import sys

base_uri = "https://api.nationalize.io/?"

while True:
    name = input("Enter a name: ")
    params = {"name": f"{name}"}
    if name == str(1):
        print("quiting...")
        sys.exit(0)
    r = requests.get(base_uri, params=params)

    print("Server Response: " + str(r.status_code))
    
    for i in r.json()["country"]:
        print(i["country_id"] + " : " + str(i["probability"]))
