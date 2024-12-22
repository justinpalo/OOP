class Spiderman:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    
class Tobey(Spiderman):
    def __init__(self,name,age,movie_title):
        super().__init__(name,age)
        self.movie_title = movie_title

class Andrew(Spiderman):
    def __init__(self,name,age,movie_title):
        super().__init__(name,age)
        self.movie_title = movie_title
        
class Tom(Spiderman):
    def __init__(self,name,age,movie_title):
        super().__init__(name,age)
        self.movie_title = movie_title
        
tobey= Tobey("Tobey Maguire", 49, "Spiderman")
andrew= Andrew("Andrew garfield", 41, "The Amazing Spiderman")
tom= Tom("Tom Holland", 28, "Spiderman: Home Coming")

print(tobey.name.upper(), tobey.movie_title)
print(andrew.name.upper(), andrew.movie_title)
print(tom.name.upper(), tom.movie_title)
        