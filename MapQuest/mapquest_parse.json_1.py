import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Brussels, Belgium"
dest = "Ghent, Belgium"
key = "3Kxgx9b8sfwMKsQndHY9GFh8au6URKfe"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)