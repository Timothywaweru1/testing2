class Dog :
    def __init__(self,name):
        self.name = name
    def bark (self):
        print(f"{self.name} says: WOOF!")  
    def sit (self):
        print(f"{self.name} sit down now")   
    def fetch (self,item):
        print(f"{self.name} go for the {item}")       
fido = Dog("Fido")
lassie = Dog("Lassie")
fido.fetch("ball")    

class Cat :
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    def sound(self):
        print(f"{self.name} always makes this sound...MEOW!")
    def sleep(self,place):
        print(f"{self.name} likes sleeping on the {place}")        
    def play(self,item):
        print(f"{self.name} is a {self.breed} and is {self.age} that likes playing with my {item}")

rose = Cat("Rose",9,"Siamese Cat")
rose.play("ball")     
rose.sleep("couch")       
rose.sound()



class Horse :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_adopted(self,owner_name):   
        self.owner_name = owner_name 
    def rename(self,new_name):
        old_name = self.name
        self.name = new_name
        print(f"{old_name} is now called {new_name}")
    def celebrate_birthday(self):   
        self.age += 1
        print(f"Happy birthday,{self.name}! You are now {self.age} years old!") 
max = Horse("Max", 10)
max.get_adopted("Sophie")
max.rename("Peter")
max.celebrate_birthday()








class Pig:
    def __init__(self,name, favorite_toy = "Any"):
        self.name = name
        self.favorite_toy = favorite_toy
molly = Pig("Molly")
result = molly.favorite_toy
print(result)




class Bird :
    def __init__(self,name,water = "Fiji water"):
        
        self.name =name
        self.water = water
tom = Bird("Tom")
print(tom.water)