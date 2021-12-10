import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "3Kxgx9b8sfwMKsQndHY9GFh8au6URKfe"

while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

    print(f"URL: {url}")

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print(f"API status: {str(json_status)} = a succesful route call.\n")
