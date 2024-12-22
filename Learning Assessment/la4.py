class ml_hero():
    def __init__(self, name, role, atk_type, basic_atk):
        self.name = name
        self.role = role
        self.atk_type = atk_type
        self.basic_atk = basic_atk

    def whoiam(self):
        return f"{self.name} is a {self.role} hero with a {self.atk_type} type attack"

m1 = ml_hero("Layla", "Marksman", "Long Range", 100)

print(m1.name)
print(m1.role)
print(m1.atk_type)
print(m1.basic_atk)
print(m1.whoiam())
