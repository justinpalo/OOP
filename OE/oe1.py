class MLBB_Hero:
    def __init__(self, name, role, dmg_type):
        self.name = name  
        self.role = role  
        self.dmg_type = dmg_type 
    def describe(self):
        return f"{self.name} is a {self.role} hero."
    def __str__(self):
        return f"{self.name} is a {self.role} and deals {self.dmg_type} damage."
        
hero1 = MLBB_Hero("Nolan", "Jungler/Assassin", "Physical Type")
hero2 = MLBB_Hero("Benedetta", "Assassin/Fighter", "Physical Type")
hero3 = MLBB_Hero("Vexana", "Mage", "Magic Type")
hero4 = MLBB_Hero("Claude", "Marksman", "Physical Type")
hero5 = MLBB_Hero("Minotaur", "Tank/Roam/Support", "Physical & True Type")

answer = str(input("Mobile Legends | press any key to enter: "))
print(f'''{answer}\nUsers Activity\nEnter game\nloading screen...\nEnter Lobby, Classic and start the game (10/10)
\nChoose your Hero...\n{hero1.describe()}\n{hero2.describe()}\n{hero3.describe()}\n{hero4.describe()}\n{hero5.describe()}
\nPlayers locked on heroes:\nS1: {hero1}\nS2: {hero2}\nS3: {hero3}\nS4: {hero4}\nS5: {hero5}''')
