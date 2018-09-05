import requests

server = "http://api.open.notify.org/"

endpoint = "iss-now.json"

response = requests.get(server+endpoint)

print(response)
