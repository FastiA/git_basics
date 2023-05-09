class Animal:
    def __init__(self, name: str, species: str, habitat: str):
        self.name = name
        self.species = species
        self.habitat = habitat
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.species}, {self.habitat})"
    
class Mammal(Animal):
    def __init__(self, name: str, species: str, habitat: str, fur_color: str):
        super().__init__(name, species, habitat)
        self.fur_color = fur_color
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.species}, {self.habitat}, {self.fur_color})"
    
class Bird(Animal):
    def __init__(self, name: str, species: str, habitat: str, wingspan: float):
        super().__init__(name, species, habitat)
        self.wingspan = wingspan
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.species}, {self.habitat}, {self.wingspan})"
    
class Fish(Animal):
    def __init__(self, name: str, species: str, habitat: str, fins: int):
        super().__init__(name, species, habitat)
        self.fins = fins
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.species}, {self.habitat}, {self.fins})"
    
class Snake(Animal):
    def __init__(self, name: str, species: str, habitat: str, venomous: bool):
        super().__init__(name, species, habitat)
        self.venomous = venomous
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.species}, {self.habitat}, {self.venomous})"
