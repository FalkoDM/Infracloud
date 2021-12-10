# import the parse functoin and get request function
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "3Kxgx9b8sfwMKsQndHY9GFh8au6URKfe"
 # break out of program with q or quit 
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest =="q":
        break
    # create API rul
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    # print the url
    print(f"URL: {url}")
    # parse the url as json and store in json_data variable
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        # if statuscode = 0 store the wanted info in variables and print out
        json_duration = json_data["route"]["formattedTime"]
        json_distance_miles = json_data["route"]["distance"]
        json_distance_kilometres = json_data["route"]["distance"] *1.61
        json_fuel_gal = json_data["route"]["fuelUsed"]
        json_fuel_liters = json_data["route"]["fuelUsed"] * 3.78
        json_bridge = json_data["route"]["hasBridge"]
        json_manouvres = json_data["route"]["legs"][0]["maneuvers"]
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
        # loop trough the json manouvers list and display narrative + distance in km
        for i in json_manouvres:
            print(f"{i['narrative']} ({round(i['distance'] * 1.61, 2)} km)")
        print("=============================================\n")
    elif json_status == 402:
        # if the statuscode is 402, display the message provided by the json data
        json_messages = json_data["info"]["messages"][0]
        print("*********************************************")
        print(f"Status code: {json_status}; {json_messages}")
        print("*********************************************\n")
    elif json_status == 611:
        json_messages = json_data["info"]["messages"][0]
        print("*********************************************")
        print(f"Status code: {json_status}; {json_messages}")
        print("*********************************************\n")
    else:
        print("*********************************************")
        print(f"For status code: {json_status}; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("*********************************************\n")
