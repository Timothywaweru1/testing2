capitals = {
    "USA" : "Washington DC",
    "Russia" : "Moscow",
    "India" : "New Delhi",
    "China" : "Bejieng",
}

capitals.update({"Kenya" : "Nairobi", "Uganda" : "Kampala"}) #you can also change the capitals of each city in the dict using update
# print(capitals)


#removing things out of dict
capitals.pop("Uganda")
# print(capitals)
capitals.popitem()
# print(capitals)
# capitals.clear()
# print(capitals)
keys = capitals.keys()
for key in capitals :
    print(key)