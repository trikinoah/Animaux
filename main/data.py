from dataclasses import dataclass

@dataclass
class Race:
    dog:str = "Dog"
    cat:str = "Cat"
    unknown:str = "N/A"

@dataclass
class Couleur:
    black:str = "Black"
    white:str = "White"
    gray:str = "Gray"
    unknown:str = "N/A"

@dataclass
class Sexe:
    male:str = "Male"
    female:str = "Female"
    unknown:str = "N/A"

@dataclass
class Pelage:
    oui:str = "Oui"
    non:str = "Non"
    unknown:str = "N/A"

@dataclass
class Cry:
    wouf:str = "Wouf !"
    miau:str = "Miau !"
    unknown:str = "N/A"
