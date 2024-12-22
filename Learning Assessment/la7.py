class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Black")
car2 = Car("Audi", "Red")

print(f"Car1 Brand: {car1.brand}")
print(f"Car1 Color: {car1.color}")
print(f"Car2 Brand: {car2.brand}")
print(f"Car2 Color: {car2.color}")

car1 = Car ("Mitsubishi", "Silver")

print(f"Updated Car1 Brand: {car1.brand}")
print(f"Updated Car1 Color: {car1.color}")
print(f"Car2 Brand: {car2.brand}")
print(f"Car2 Color: {car2.color}")