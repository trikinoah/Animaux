from data import Race, Sexe, Couleur, Cry
from animal import Animal

class Cat(Animal):
    def __init__(self, name: str = "N/A", age: int = "N/A", sexe: str = Sexe.unknown, couleur:str = Couleur.unknown):
        super().__init__(Race.cat, name, age, sexe, Cry.miau)
        self.couleur = couleur

    def description(self):
        super().description()
        print("Couleur: " + self.couleur)

