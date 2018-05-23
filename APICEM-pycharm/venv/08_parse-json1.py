import urllib.parse
import requests

main_api = "https://maps.googleapis.com/maps/api/geocode/json?"
address = "san jose"
key = "AIzaSyAjBDAYgIljM4EseTmsdRoqFHya3M4CIZQ"
url = main_api + urllib.parse.urlencode({"address": address, "key": key})

json_data = requests.get(url).json()
print(json_data)