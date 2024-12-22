class AnimeCharacter:
    def __init__(self,name,ability):
        self.name = name
        self.ability = ability
    def Introduce(self,new_func):
        def opening(*args, **kwargs):
            print("Introducing...")
            new_func(*args, **kwargs)
            print("This charcater is amazing!")
        return opening
           
       
char1 = AnimeCharacter ("Eppoloks", "Triple Booking")

@char1.Introduce
def charcater_intro(char_name, char_ability):
    print(f"I am {char_name} and I can use {char_ability}")
charcater_intro("Eppoloks", "Triple Booking")    