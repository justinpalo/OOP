from abc import ABC, abstractmethod

class NinjaTurtles(ABC):
    def __init__(self, real_name, __alias):
       self.real_name = real_name
    @property
    @abstractmethod
    def __init__(self, real_name):
        pass

class Leonardo (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name 
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias

class MichaelAngelo (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name 
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias     

class Donatello (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name 
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias

class Raphael (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name 
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias

pagong1 = Leonardo ("Leonardo", "NiwNiw")
pagong2 = MichaelAngelo ("MichaelAngelo", "NitNit")
pagong3 = Donatello("Donatello", "MitchiBoy")
pagong4 = Raphael ("Raphael", "Labo")



