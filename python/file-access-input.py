while True:
    newitem = input("Enter device name: ")
    if newitem == "exit":
        print("All done!")
        break
    else:
        file = open("devices.txt", "a")
        file.write(newitem+"\n")
        file.close()
