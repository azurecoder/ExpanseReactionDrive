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

    def find_closest_distance(self, other_planet, time_steps_per_day: int = 24) -> tuple:
        """
        Calculate the closest distance to another planet in the future.

        :param other_planet: The Planet instance to calculate the closest distance to.
        :param time_steps_per_day: Number of steps per day (e.g., 24 for hourly).
        :return: Tuple (closest_distance_in_AU, day_of_year, year).
        """
        from datetime import datetime

        # Get current date
        today = datetime.now()
        current_year = today.year
        current_day_of_year = today.timetuple().tm_yday

        # Use the longer orbital period for iteration
        farther_period = max(self.period, other_planet.period)
        closest_distance = float('inf')
        closest_time = None

        # Start from the current day and year
        for step in range(int(farther_period * time_steps_per_day)):
            # Calculate the day and year for the current step
            day_of_year = (current_day_of_year + (step / time_steps_per_day)) % 365
            year = current_year + ((current_day_of_year + (step / time_steps_per_day)) // 365)

            # Get distances
            distance_self = self.get_orbital_distance(day_of_year, year)
            distance_other = other_planet.get_orbital_distance(day_of_year, year)

            # Compute relative distance
            relative_distance = abs(distance_self - distance_other)

            if relative_distance < closest_distance:
                closest_distance = relative_distance
                closest_time = (day_of_year, year)

        return closest_distance, closest_time
