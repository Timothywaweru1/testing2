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