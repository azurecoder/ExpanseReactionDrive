import math

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