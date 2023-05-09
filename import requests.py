import requests
import sys

url = "https://api.nationalize.io/?name="

while True:
    name = input("Enter a name: ")

    if name == str(1):
        print("quiting...")
        sys.exit(0)
    r = requests.get(url + name)

    print("Server Response: " + str(r.status_code))
    for i in r.json()["country"]:
        print(i["country_id"] + " : " + str(i["probability"]))
