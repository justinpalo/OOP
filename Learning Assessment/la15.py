class Dog():
    def __init__(self,name):
        self.name= name
    
    def speak(self):
        print("Bark!")

class Cat():
    def __init__(self,name):
        self.name= name
    def speak(self):
        print("Meow!")    

class Bird():
    def __init__(self,name):
        self.name= name        
    def speak(self):
        print("Chirp!")    

class Fish():
    def __init__(self,name):
        self.name= name        
    def speak(self):
        return f"..."

dog = Dog("Mark")
cat = Cat("Justin")
bird = Bird("Eppo")
fish = Fish("NiwtNiwt")

def animal_sound(animal):
    animal.speak()
    
for x in (dog,cat,bird,fish):
    animal_sound(x)