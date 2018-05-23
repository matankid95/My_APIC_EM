import urllib.parse
import requests

main_api = "https://maps.googleapis.com/maps/api/geocode/json?"
address = "san jose"
key = "AIzaSyAjBDAYgIljM4EseTmsdRoqFHya3M4CIZQ"
url = main_api + urllib.parse.urlencode({"address": address, "key": key})

json_data = requests.get(url).json()
print(url)
json_status = json_data["status"]
print("API Status: " + json_status)

formatted_address = json_data["results"][0]["formatted_address"]
print(formatted_address)
