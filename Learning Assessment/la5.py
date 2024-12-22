class mlbb:
    def __init__(self, name, role, hero_type):
        self.name = name
        self.role = role
        self.hero_type = hero_type

    def describe(self):
        return f"{self.name} is a {self.role} and {self.role} and {self.hero_type}"

hero1 = mlbb ("Zilong", "Figther", "Damage") 
hero2 = mlbb ("Kadita", "Mage", "Damage")   

print(f'''{hero1.describe()}
{hero2.describe()}
''')