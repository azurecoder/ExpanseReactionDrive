from enum import Enum

class StarType(Enum):
    """
    Basic spectral classes of stars in cosmology/astronomy, 
    roughly ordered from hottest (O-type) to coolest (M-type).
    """
    O = "O-type (very hot, blue stars)"
    B = "B-type (blue-white stars)"
    A = "A-type (white stars)"
    F = "F-type (yellow-white stars)"
    G = "G-type (yellow stars like the Sun)" 
    K = "K-type (orange stars)" 
    M = "M-type (red stars, includes most red dwarfs)"  # Coolest stars

class Star:
    def __init__(self, name: str, solar_mass, star_type: StarType):
        self.name = name
        self.star_type = star_type
        self.solar_mass = solar_mass

    def __str__(self):
        return f"{self.name} is a {self.star_type.name} star."

    def __repr__(self):
        return f"Star({self.name}, {self.star_type})"
    
    def __eq__(self, other):
        return self.name == other.name and self.star_type == other.star_type
    
    @property
    def name(self): return self._name

    @property
    def type(self): return self._star_type

    @property
    def mass(self): return self._solar_mass
