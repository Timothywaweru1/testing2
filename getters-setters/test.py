class Dog:
    count = 0
    dog_list = []
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age
        self.get_count()
        self.get_dog_list(self)
    def sound (self):
        print(f"{self.name} likes saying WOOOF!")
    def fav_toy(self,play_toy):
        print(f"{self.name} plays {play_toy} too much")
    @classmethod
    def get_count(cls):
        cls.count += 1
    @classmethod
    def get_dog_list(cls,dog_collection):
        cls.dog_list.append(dog_collection)    
dog1 = Dog("Rubia","German shepherd", 10)
dog2 = Dog("Spot","American Bulldog", 5)
print(Dog.count)
print(Dog.dog_list)


