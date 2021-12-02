list1 = []

while True:
    listitem = input("Geef een item om in de lijst te plaatsen: ")
    if listitem is not "q":
        list1.append(listitem)
        print(list1)
        print(type(list1))
    else:
        break