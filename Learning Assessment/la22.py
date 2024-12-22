class Birthday():
    def __init__(self,theme,main_dish):
        self.theme = theme
        self.main_dish = main_dish
    
    def __my_dish(self):
        print(self.main_dish)
    
    def dishsksks(self):
        print("itlog")
        self.__my_dish()
        
        
dish1 = Birthday("year end party","binangkol")
dish2 = Birthday("socializing","pancit bato? dinuguan")
dish3 = Birthday("team building","bulala yung sinusupsop")

dish1.dishsksks()
dish2.dishsksks()
dish3.dishsksks()