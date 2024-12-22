class Hero:
    def __init__(self,name,health,atk_pwr):
        self.name = name
        self.health = health
        self.atk_pwr = atk_pwr
    def bsc_atk(self,target):
        target.health = target.health - self.atk_pwr
    def heal(self,heal):
        heal.health = heal.health + self.health

niwniw =  Hero ("Niwniwsksk", 1200, 400)
nitnit = Hero ("Nitnitsksk", 1400, 300)

print(niwniw.name, niwniw.health, "HP", niwniw.atk_pwr, "Damage")
print(nitnit.name, nitnit.health, "HP", nitnit.atk_pwr, "Damage")
niwniw.bsc_atk(nitnit)
print(niwniw.name, niwniw.health, "HP", niwniw.atk_pwr, "Damage")
print(nitnit.name, nitnit.health, "HP", nitnit.atk_pwr, "Damage")
nitnit.heal(niwniw)
niwniw.bsc_atk(nitnit)
print(niwniw.name, niwniw.health, "HP", niwniw.atk_pwr, "Damage")
print(nitnit.name, nitnit.health, "HP", nitnit.atk_pwr, "Damage")
niwniw.bsc_atk(nitnit)
print(niwniw.name, niwniw.health, "HP", niwniw.atk_pwr, "Damage")
print(nitnit.name, nitnit.health, "HP", nitnit.atk_pwr, "Damage")
niwniw.bsc_atk(nitnit)
print(niwniw.name, niwniw.health, "HP", niwniw.atk_pwr, "Damage")
print(nitnit.name, nitnit.health, "HP", nitnit.atk_pwr, "Damage")