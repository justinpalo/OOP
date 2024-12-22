class ml_hero():
    def __init__(self, name, basic_atk, role, atk_type):
        self.name = name
        self.basic_atk = basic_atk
        self.role = role
        self.atk_type = atk_type

m1 = ml_hero ("Layla", 100, "Marksman", "Long Range")

print(m1.name)
print(m1.basic_atk)
print(m1.role)
print(m1.atk_type)