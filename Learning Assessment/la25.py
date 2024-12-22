from abc import ABC, abstractmethod

class Character(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
class Batman(Character):
    def __init__ (self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias
    @property
    def name(self): 
        return self.__alias

hero = Batman ("Bruce Wayne", "Batman")
print(hero.name)        