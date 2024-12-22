class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def DescribeToy(self):
        print(f"The name of niwniw toy product is {self.name} with a budget price {self.price}.")
class Car (Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

toy = Toy ("marwinqtpie", "20 betot")
toy.DescribeToy()                
    