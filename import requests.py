import requests

r = requests.get('https://api.nationalize.io/?name=michael')

print(r.status_code)
print(r.json())