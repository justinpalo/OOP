class Favorite_food:
    def __init__(self,main_ingr,sec_ingr,thr_ingr):
        self.__main_ingr = main_ingr
        self.__sec_ingr = sec_ingr
        self.__thr_ingr = thr_ingr
    def __str__(self):
        return f"My favorite food dessert are have {self.__main_ingr}, {self.__sec_ingr}, and {self.__thr_ingr}."
mango_graham_cake = Favorite_food("graham","kremdensada","mango")
turon = Favorite_food("banana", "sugar", "JackFruit")
leche_plan = Favorite_food("egg yolk", "vanilla", "sugar")
print(mango_graham_cake)
print(turon)
print(leche_plan)