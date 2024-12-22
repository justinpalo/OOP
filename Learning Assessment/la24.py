from abc import ABC, abstractmethod 

class GameCharacter (ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def attack(self):
        pass
    
class Warrior(GameCharacter):
    def attack(self):
        print(f"Swings sword!")
class Mage(GameCharacter):
    def attack(self):
        print(f"Casts a fireball!")
class Archer(GameCharacter):
    def attack(self):
        print(f"Shoots an arrow!")
class Healer(GameCharacter):
    def attack(self):
        print(f"Casts healing spell on ally!")
        
warrior = Warrior ("Mark")
mage = Mage ("Justin")
archer = Archer ("Eppo")
healer = Healer ("Laladoyz")

warrior.attack()
mage.attack()
archer.attack()
healer.attack()