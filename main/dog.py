from data import Race, Sexe, Pelage, Cry
from animal import Animal

class Dog(Animal):
    def __init__(self, name: str = "N/A", age: int = "N/A", sexe: str = Sexe.unknown, pelage:str = Pelage.unknown):
        super().__init__(Race.dog, name, age, sexe, Cry.wouf)
        self.pelage = pelage

    def description(self):
        super().description()
        print("Pelage: " + self.pelage)
        
    def bark(self) -> str:
        """
        return the song of dog emit
        """
        return "Woof!"