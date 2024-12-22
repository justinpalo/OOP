class Appliances():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def operate(self):
        print("Operating")
    
    def info(self):
        print(f"Brand: {self.brand} Model: {self.model}")
    
class WashingMachine(Appliances):
    def operate(self):
        print("Washing clothes!")
        
class Refrigator(Appliances):
    def operate(self):
        print("Keeping foood cold!")
        
class Microwave(Appliances):
    def operate(self):
        print("Heating food!")
        
washing =WashingMachine ("LG TurboWash", "360 WM4000HBA")
ref = Refrigator("Fujidenzo", "RDD-60 S")
microwave = Microwave("Toshib", "MM-EG25P(BK)")

for x in [washing, ref, microwave]:
    x.operate()
    x.info()            