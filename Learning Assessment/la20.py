class Favorite_food:
    def __init__(self,main_ingr,sec_ingr,thr_ingr):
        self.main_ingr = main_ingr #public
        self._sec_ingr = sec_ingr #protected
        self.__thr_ingr = thr_ingr #private
    def __str__(self):
        return f"My favorite food dessert are have {self.__main_ingr}, {self.__sec_ingr}, and {self.__thr_ingr}."
    def dessertsksk(self,age):
        if age >= 18:
           return self.__thr_ingr
        else:
            return "secret"  
mango_graham_cake = Favorite_food("graham","kremdensada","mango")
turon = Favorite_food("banana", "sugar", "JackFruit")
leche_plan = Favorite_food("egg yolk", "vanilla", "sugar")
print(mango_graham_cake.dessertsksk(17))
print(turon.dessertsksk(18))
print(leche_plan.dessertsksk(25))