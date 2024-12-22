class Animal: 
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def DescribeAnimal(self):
        print(f"The animal is {self.name} with the type of {self.type}.")

class Fish (Animal):
        def __init__(self, name, type, can_swim):
            super().__init__(name, type)           
            self.can_swim = True

fish = Fish ("Galagunggong", "Isda", True)
fish.DescribeAnimal()
print(fish.can_swim)            