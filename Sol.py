from StarType import Star, StarType, Planet, PlanetType, EllipticalOrbit
import math

class Sol(Star):
    def __init__(self):
        super().__init__("Sol", 1.0, StarType.G)

class Earth(Planet):
    AU_IN_KM = 149597879
    def __init__(self, orbit: EllipticalOrbit):
        super().__init__("Earth", 1.0, 1.0, PlanetType.TERRESTRIAL, orbit)

if __name__ == "__main__":
    sol = Sol()
    earth_orbit = EllipticalOrbit(0.0167, 1.0, 3.0, 365, sol)
    earth = Earth(earth_orbit)  
    print(f"Closest approach to Earth: {earth.get_closest_approach()}")
    print(f"Farthest approach from Earth: {earth.get_farthest_approach()}")
    print(f"Orbital distance in km on 5th of Feb: {int(round(earth.get_orbital_distance(36.0) * Earth.AU_IN_KM, 0)): ,} km") # February 5th