class Vehicle:
    def __init__(self, brand, model, fuel_typ):
        self.brand = brand
        self.model = model
        self.fuel_typ = fuel_typ

    def DescribeVehicle(self):
        return f"This my vehicle {self.brand} is a {self.model} model and the fuel type is {self.fuel_typ}."

class Car(Vehicle):
    pass
class Motorcycle(Vehicle):
    pass

v1 = Car ("Toyota Corolla", "2024", "Gasoline")
v2 = Motorcycle ("Rs125", "2016", "Unleaded")
print(v1.DescribeVehicle())
print(v2.DescribeVehicle())

        