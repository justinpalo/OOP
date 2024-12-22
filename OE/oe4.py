class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name}! {target.name}'s remaining health: {target.health}")

    def defend(self, damage):
        self.health -= max(0, damage - 5)  
        print(f"{self.name} defends! Remaining health: {self.health}")

    def special_move(self, target=None):
        pass

class Warrior(Character):
    def special_move(self):
        self.power *= 2
        print("Warrior uses Shield Bash!")

class Mage(Character):
    def special_move(self, target):
        target.health -= 188
        print("Mage casts Fireball!")

class Marksman(Character):
    def special_move(self, target):
        target.health -= self.power
        print("Marksman shoots Piercing Arrow!")

class Villain(Character):
    def special_move(self):
        self.health += 40
        print("Villain roars and gains health!")


warrior = Warrior("Warrior", 100, 20)
mage = Mage("Mage", 80, 15)
marksman = Marksman("Marksman", 90, 10)
villain = Villain("Villain", 120, 5)

characters = [warrior, mage, marksman, villain]

for character in characters:
    if isinstance(character, (Mage, Marksman)):
        character.special_move(villain)  
    else:
        character.special_move()
    character.attack(villain)
    villain.defend(character.power)  