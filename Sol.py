from StarType import Star, StarType, Planet, PlanetType, EllipticalOrbit
import math

class Sol(Star):
    AU_IN_KM = 149597879
    def __init__(self):
        super().__init__("Sol", 1.0, StarType.G)

class Earth(Planet):
    def __init__(self, orbit: EllipticalOrbit):
        super().__init__("Earth", 1.0, 1.0, PlanetType.TERRESTRIAL, orbit)

class Mars(Planet):
    def __init__(self, orbit: EllipticalOrbit):
        super().__init__("Mars", 0.107, 0.532, PlanetType.TERRESTRIAL, orbit)

