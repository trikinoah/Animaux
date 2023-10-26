from animal import Animal
from data import (Pelage,
                  Race,
                  Sexe,
                  Cry,
                  Couleur)
from dog import Dog
from cat import Cat

animal1 = Animal(Race.dog,
                 "toto",
                 11, Sexe.male)
animal2 = Animal(Race.cat, "nono", 5, Sexe.female)
animal3 = Cat('pepe',1,Sexe.female, Couleur.black)
animal4 = Dog()
# for animal in Animal.animaux:
#     animal.description()
print(animal4.bark())
Animal.count()