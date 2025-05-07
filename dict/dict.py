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

#dict mapping
day_map = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
day_map_no = 6
print(day_map.get(day_map_no, "invalid day"))



#mapping into funcs
def mul (a,b) :
    return a * b
def div (a,b) :
    return a / b
def add (a,b) :
    return a + b
def sub (a,b) :
    return a - b

dict_sol = {
    "ad" : add,
    "subtract" : sub,
    "multiply" : mul,
    "divide" : div,
}
want_required_sol = "divide"
result = dict_sol.get("divide")(100,5)
print(result)


math_map = {
    "double" : lambda x : x * 2,
    "square" : lambda x : x ** 2,
    "negate" : lambda x : -x,
}
op = "square"
number = 5
result = math_map[op](number)
print(result)