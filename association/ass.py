class GroceryItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Shopper:
    def __init__(self,name):
        self.name = name
        self.grocery_items = []
shopper = Shopper("Alice")
item_1 = GroceryItem("apple",1)
item_2 = GroceryItem("banana",3)     
shopper.grocery_items.append(item_1)
shopper.grocery_items.append(item_2)  
# for item in shopper.grocery_items:
#     print(item.name,item.price)         
print(shopper.grocery_items)
for item in shopper.grocery_items:
    print(item.name)