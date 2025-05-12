class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):   
        print(f"{self.name} goes WOOOO!") 
rex = Dog("Rex")
rex.bark()                                                      