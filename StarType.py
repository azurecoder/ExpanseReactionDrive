from enum import Enum
import math

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

class PlanetType(Enum):
    TERRESTRIAL = "Rocky planet (like Earth or Mars)"
    GAS_GIANT = "Gas giant (like Jupiter or Saturn)"
    ICE_GIANT = "Ice giant (like Uranus or Neptune)"
    DWARF_PLANET = "Small, non-satellite body (like Pluto or Ceres)"
    HOT_JUPITER = "Gas giant orbiting very close to its star"
    SUPER_EARTH = "Planet larger than Earth but smaller than Neptune"
    MINI_NEPTUNE = "Planet smaller than Neptune but bigger than Earth"
    OCEAN_WORLD = "Possible planet with significant surface or subsurface oceans"

class Star:
    def __init__(self, name: str, solar_mass, star_type: StarType):
        self._name = name
        self._star_type = star_type
        self._solar_mass = solar_mass

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

class EllipticalOrbit:
    def __init__(self, eccentricity, semi_major_axis, perihelion_day, perihelion_year, period, star):
        """
        Initializes an elliptical orbit.

        :param eccentricity: The orbital eccentricity (e).
        :param semi_major_axis: Semi-major axis of the orbit (in AU).
        :param perihelion_day: Day of the perihelion in the specified perihelion_year.
        :param perihelion_year: Year of the perihelion event.
        :param period: Orbital period (in Earth days).
        :param star: The star around which the object orbits (must have a name attribute).
        """
        self._eccentricity = eccentricity
        self._semi_major_axis = semi_major_axis
        self._star = star
        self._perihelion_day = perihelion_day
        self._perihelion_year = perihelion_year
        self._period = period

    def __str__(self):
        return f"An elliptical orbit around {self._star.name}."

    def __repr__(self):
        return f"EllipticalOrbit({self._star})"

    def __eq__(self, other):
        return (
            self.eccentricity == other.eccentricity and 
            self._semi_major_axis == other.semi_major_axis and
            self._perihelion_day == other.perihelion_day and
            self._perihelion_year == other.perihelion_year
        )

    @property
    def eccentricity(self): return self._eccentricity

    @property
    def semi_major_axis(self): return self._semi_major_axis

    @property
    def star(self): return self._star

    @property
    def perihelion_day(self): return self._perihelion_day

    @property
    def perihelion_year(self): return self._perihelion_year

    @property
    def period(self): return self._period

    def get_distance(self, day_of_year: float, year: int) -> float:
        """
        Returns the orbital distance (in AU) from the star at a given day of the year and year.

        The formula for distance in an elliptical orbit:
            r(theta) = a * (1 - e^2) / (1 + e * cos(theta))

        :param day_of_year: Day of the year (0–365).
        :param year: The calendar year for which the distance is calculated.
        :return: Distance from the star (in AU).
        """
        import math

        # Calculate the total elapsed days since the last perihelion
        days_elapsed = (year - self.perihelion_year) * 365 + (day_of_year - self.perihelion_day)

        # Mean motion (radians per day)
        n = 2.0 * math.pi / self.period

        # Orbital angle in radians from perihelion
        theta = n * days_elapsed

        # Compute distance using the orbital equation
        a = self._semi_major_axis
        e = self._eccentricity
        r = a * (1 - e**2) / (1 + e * math.cos(theta))
        return r

    def get_closest_approach(self):
        """
        Returns a tuple of (perihelion_day, perihelion_year, distance) for the perihelion.
        """
        a = self._semi_major_axis
        e = self._eccentricity
        day = self._perihelion_day
        year = self._perihelion_year
        distance = a * (1 - e)  # Perihelion distance
        return day, year, distance

    def get_farthest_approach(self):
        """
        Returns a tuple of (day_of_year, year, distance) for the aphelion.
        Aphelion is approximately half an orbital period (in days) after perihelion.
        """
        a = self._semi_major_axis
        e = self._eccentricity
        # Aphelion occurs about half an orbital period after perihelion
        aphelion_elapsed_days = self.period / 2.0

        # Calculate the aphelion date
        total_days = self._perihelion_day + aphelion_elapsed_days
        year_increment = int(total_days // 365)
        aphelion_day = total_days % 365

        year = self._perihelion_year + year_increment
        distance = a * (1 + e)  # Aphelion distance
        return aphelion_day, year, distance
    
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
