class ml_hero():
    def __init__(self, name, atk_type):
        self.name = name
        self.atk_type = atk_type

    def who(self):
        return f"{self.name} has a attack type of {self.atk_type}"    

m1 = ml_hero("Layla", "Long Range")
print(m1.who())    