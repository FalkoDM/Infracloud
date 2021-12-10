import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "3Kxgx9b8sfwMKsQndHY9GFh8au6URKfe"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest =="q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

    print(f"URL: {url}")

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    json_duration = json_data["route"]["formattedTime"]
    json_distance_miles = json_data["route"]["distance"]
    json_distance_kilometres = json_data["route"]["distance"] *1.61
    json_fuel_gal = json_data["route"]["fuelUsed"]
    json_fuel_liters = json_data["route"]["fuelUsed"] * 3.78
    json_bridge = json_data["route"]["hasBridge"]
    json_manouvres = json_data["route"]["legs"][0]["maneuvers"]

    if json_status == 0:
        print(f"API status: {str(json_status)} = a succesful route call.\n")
        print("=============================================")
        print(f"Directions from {orig} to {dest}")
        print(f"Trip Duration: {json_duration}")
        print(f"Miles: {json_distance_miles}")
        print(f"Kilometers: {str('{:.2f}'.format(json_distance_kilometres))}")
        print(f"Fuel Used (Gal): {json_fuel_gal}")
        print(f"Fuel used (Ltr): {round(json_fuel_liters, 2)}")
        if json_bridge == True:
            print("route has a bridge")
        if json_bridge == False:
            print("route has no bridge")
        print("=============================================")
        for i in json_manouvres:
            print(f"{i['narrative']} ({round(i['distance'] * 1.61, 2)} km)")
        print("=============================================\n")