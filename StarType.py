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
    def __init__(self, eccentricity, semi_major_axis, perihelion_day, period, star: Star):
        self._eccentricity = eccentricity
        self._semi_major_axis = semi_major_axis
        self._star = star
        self._perihelion_day = perihelion_day
        self._period = period

    def __str__(self):
        return f"An elliptical orbit around {self._star.name}."

    def __repr__(self):
        return f"EllipticalOrbit({self._star})"

    def __eq__(self, other):
        return self.eccentricity == other.eccentricity and self._semi_major_axis == other.semi_major_axis

    @property
    def eccentricity(self): return self._eccentricity

    @property
    def semi_major_axis(self): return self._semi_major_axis

    @property
    def star(self): return self._star

    @property
    def perihelion_day(self): return self._perihelion_day

    @property
    def period(self): return self._period

    def get_distance(self, day_of_year: float) -> float:
        """
        Returns the orbital distance (in AU) from the star at a given day of the year (0–365).
        
        We assume:
          - day_of_year = 0 is Jan 1,
          - perihelion occurs around day_of_year = 3 (Jan 3).
        
        The formula for distance in an elliptical orbit (assuming perihelion at angle = 0):
            r(theta) = a * (1 - e^2) / (1 + e * cos(theta))
        
        Here:
            a = semi-major axis
            e = eccentricity
            theta = mean orbital angle from perihelion
        """
        # Mean motion (radians per day)
        n = 2.0 * math.pi / self.period

        # Shift day_of_year so that day_of_year = self._perihelion_day => theta = 0
        delta_days = day_of_year - self.perihelion_day
        # The orbital angle in radians from perihelion
        theta = n * delta_days

        # Compute distance using the orbital equation
        a = self._semi_major_axis
        e = self._eccentricity
        r = a * (1 - e**2) / (1 + e * math.cos(theta))
        return r

    def get_closest_approach(self):
        """
        Returns a tuple of (day_of_year, distance) for the approximate perihelion.
        For a simple model with argument_of_perihelion = 0, 
        perihelion is day_of_year = _perihelion_day, distance = a(1 - e).
        """
        a = self._semi_major_axis
        e = self._eccentricity
        day = self._perihelion_day
        distance = a * (1 - e)  # Perihelion distance
        return day, distance

    def get_farthest_approach(self):
        """
        Returns a tuple of (day_of_year, distance) for the approximate aphelion.
        In our simplified model, aphelion is about half an orbital period 
        ( ~182 days ) away from perihelion.
        """
        a = self._semi_major_axis
        e = self._eccentricity
        # Aphelion occurs about half an orbital period after perihelion
        day = self._perihelion_day + self.period / 2.0
        # Wrap day of year to 0–365 range (mod 365)
        day = day % self.period

        distance = a * (1 + e)  # Aphelion distance
        return day, distance
    
class Planet:
    def __init__(self, name: str, mass, radius, type: PlanetType, orbit: EllipticalOrbit):
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

    def get_orbital_distance(self, day_of_year: float) -> float:
        return self._orbit.get_distance(day_of_year)
    
    def get_closest_approach(self):
        return self._orbit.get_closest_approach()
    
    def get_farthest_approach(self):
        return self._orbit.get_farthest_approach()