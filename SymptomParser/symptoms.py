import requests

POST_URL = "https://api.infermedica.com/v2/symptoms"

header = { "app_id" : "9cfcafae", "app_key" : "55b78a933718c8e68ba37f2f8d80b1a7"}

r = requests.get(POST_URL, headers=header)

json = r.json()

for key in json:
	print(key['name'] + " " + key['id'])
