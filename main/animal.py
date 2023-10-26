from data import Race, Sexe, Cry

class Animal:
    animaux : list = []

    def __init__(self,race : str = Race.unknown, name : str = "N/A", age : int = "N/A", sexe: str = Sexe.unknown, cry:str = Cry.unknown):
        self.name = name
        self.race = race
        self.age = age
        self.sexe = sexe
        self.cry = cry
        Animal.animaux.append(self)
    
    def description(self):
        print("Race: " + self.race)
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Genre: " + self.sexe)
        print("Cry: " + self.cry)

    @staticmethod
    def count():
        nbanimaux:int = len(Animal.animaux)
        print("Nb animaux : " + str(nbanimaux))

