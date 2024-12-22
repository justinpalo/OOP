class Phone: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def DescribePhone(self):
        return f"My phone is an {self.brand} brand and the model is {self.model}."
    
class Android(Phone):
    def __init__(self, brand, model):
        super().__init__(brand, model)

phone = Android("Android", "Samsung A03")
print(phone.DescribePhone())            