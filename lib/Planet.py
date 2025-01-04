from lib.PlanetType import PlanetType
from lib.EllipticalOrbit import EllipticalOrbit

class Planet:
    def __init__(self, name: str, mass, radius, type: PlanetType, orbit: EllipticalOrbit):
        """
        Initializes a planet object.

        :param name: Name of the planet.
        :param mass: Mass of the planet.
        :param radius: Radius of the planet.
        :param type: Type of the planet (e.g., terrestrial, gas giant).
        :param orbit: Elliptical orbit of the planet.
        """
        self._name = name
        self._mass = mass
        self._radius = radius
        self._star = orbit.star
        self._type = type
        self._orbit = orbit

    def __str__(self):
        return f"{self.name} is a planet orbiting {self.star.name}."

    def __repr__(self):
        return f"Planet({self.name}, {self.star})"

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type and self.star == other.star

    @property
    def name(self): return self._name

    @property
    def mass(self): return self._mass

    @property
    def radius(self): return self._radius

    @property
    def star(self): return self._star

    @property
    def type(self): return self._type

    @property
    def period(self): return self._orbit.period

    def get_orbital_distance(self, day_of_year: float, year: int) -> float:
        """
        Returns the orbital distance from the star on a given day of the year and year.

        :param day_of_year: Day of the year (0-365).
        :param year: Year for the calculation.
        :return: Orbital distance (in AU).
        """
        return self._orbit.get_distance(day_of_year, year)

    def get_closest_approach(self):
        """
        Returns the closest approach to the star (perihelion).

        :return: Tuple (perihelion_day, perihelion_year, distance).
        """
        return self._orbit.get_closest_approach()

    def get_farthest_approach(self):
        """
        Returns the farthest approach to the star (aphelion).

        :return: Tuple (aphelion_day, aphelion_year, distance).
        """
        return self._orbit.get_farthest_approach()
