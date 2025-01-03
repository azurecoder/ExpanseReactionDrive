from StarType import EllipticalOrbit
from Sol import Sol, Earth
import math

if __name__ == "__main__":
    sol = Sol()
    earth_orbit = EllipticalOrbit(0.0167, 1.0, 3.0, 2024, 365, sol)
    mars_orbit = EllipticalOrbit(0.0934, 1.524, 129.0, 2024, 687, sol)
    earth = Earth(earth_orbit)  
    mars = Earth(mars_orbit)  
    # Get all of the details for Earth 
    print("Details for Earth: ---->")
    print(f"Closest approach to Sun: {earth.get_closest_approach()}")
    print(f"Farthest approach from Sun: {earth.get_farthest_approach()}")
    print(f"Orbital distance in km on 5th of Feb: {int(round(earth.get_orbital_distance(36.0, 2025) * Sol.AU_IN_KM, 0)): ,} km") # February 5th
    print("Details for Mars: ---->")
    print(f"Closest approach to Sun: {mars.get_closest_approach()}")
    print(f"Farthest approach from Sun: {mars.get_farthest_approach()}")
    print(f"Orbital distance in km on 5th of Feb: {int(round(mars.get_orbital_distance(36.0, 2025) * Sol.AU_IN_KM, 0)): ,} km") # February 5th

