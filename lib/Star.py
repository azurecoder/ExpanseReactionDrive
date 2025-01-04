from lib.StarType import StarType

class Star:
    def __init__(self, name: str, solar_mass, star_type: StarType, AU_IN_KM=149597879):
        self._name = name
        self._star_type = star_type
        self._solar_mass = solar_mass
        self._au_in_km = AU_IN_KM

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

    @property
    def au_in_km(self): return self._au_in_km