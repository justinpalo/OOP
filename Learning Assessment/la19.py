class Favorite_food:
    def __init__(self,main_ingr,sec_ingr,thr_ingr):
        self.main_ingr = main_ingr
        self._sec_ingr = sec_ingr
        self.__thr_ingr = thr_ingr
    def __str__(self):
        return f"My favorite food dessert are have {self.main_ingr}, {self._sec_ingr}, and {self.__thr_ingr}."
mango_graham_cake = Favorite_food("graham","kremdensada","mango")
turon = Favorite_food("banana", "sugar", "JackFruit")
leche_plan = Favorite_food("egg yolk", "vanilla", "sugar")
print(mango_graham_cake.__thr_ingr)
print(turon.__thr_ingr)
print(leche_plan.__thr_ingr)