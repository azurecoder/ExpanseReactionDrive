import math
from datetime import datetime, timedelta

class MissionCalculator:
    def __init__(self, distance_au=0.524, fuel_mass_kg=200000, dry_mass_kg=15500, fuel_type="liquid", sustained_accel=0.5):
        """
        Initialize the mission parameters.
        :param distance_au: Distance to Mars in AU (default is 0.524 AU at closest approach).
        :param fuel_mass_kg: Total fuel carried by the spacecraft in kg.
        :param dry_mass_kg: Dry mass of the spacecraft (excluding fuel).
        :param fuel_type: Type of fuel used ("liquid" or "solid").
        :param sustained_accel: Maximum acceleration in multiples of Earth's gravity (g = 9.81 m/s²).
        """
        self.distance_km = distance_au * 149597870.7  # Convert AU to km
        self.dry_mass = dry_mass_kg
        self.fuel_mass = fuel_mass_kg
        self.fuel_type = fuel_type
        self.sustained_accel = sustained_accel  # Desired acceleration in g-force
        self.g = 9.81  # Gravity in m/s²

        # Fuel-specific impulse (ISP) in seconds
        self.fuel_efficiency = {
            "liquid": 450,   # ISP for liquid fuel (~450s for LOX/LH2)
            "solid": 250     # ISP for solid fuel (~250s for solid rocket motors)
        }

        if fuel_type not in self.fuel_efficiency:
            raise ValueError("Fuel type must be 'liquid' or 'solid'.")

    def calculate_mission_time(self):
        """
        Compute acceleration, coasting, and deceleration time while respecting available fuel mass.
        Returns:
            - Total travel time in days
            - Time spent accelerating and decelerating
            - Peak velocity before coasting
            - Estimated fuel consumption
            - Estimated arrival date
        """
        # Convert distance to meters
        distance_m = self.distance_km * 1000  

        # Effective exhaust velocity (Ve = ISP * g)
        exhaust_velocity = self.fuel_efficiency[self.fuel_type] * self.g  # m/s

        # Compute total mass at start and end of burn
        initial_mass = self.dry_mass + self.fuel_mass  # Total mass with fuel
        final_mass = self.dry_mass  # Mass after all fuel is burned

        # Compute thrust using F = ma
        acceleration_m_s2 = self.sustained_accel * self.g  # m/s²
        thrust_newtons = initial_mass * acceleration_m_s2  # F = m * a

        # Compute correct mass flow rate using ṁ = T / Ve
        mass_flow_rate = thrust_newtons / exhaust_velocity  # kg/s
        burn_time_s = self.fuel_mass / mass_flow_rate  # Time until fuel runs out
        burn_time_days = burn_time_s / (60 * 60 * 24)  # Convert to days

        # Print burn time for debugging
        print(f"Burn time (s): {burn_time_s}")  # Should vary with fuel mass

        # Compute peak velocity using v = a * t
        peak_velocity_m_s = acceleration_m_s2 * burn_time_s

        # Compute distance covered during burn phase
        distance_covered_m = 0.5 * acceleration_m_s2 * burn_time_s**2  

        # Check if fuel is enough to reach halfway point
        if distance_covered_m >= distance_m / 2:
            # Fuel is sufficient for full acceleration phase
            accel_time_days = burn_time_days
            coasting_time_days = ((distance_m - 2 * distance_covered_m) / (2 * peak_velocity_m_s)) / (60 * 60 * 24)
        else:
            # Fuel runs out before reaching halfway point, switch to coasting early
            accel_time_days = burn_time_days
            coasting_time_days = ((distance_m - 2 * distance_covered_m) / (2 * peak_velocity_m_s)) / (60 * 60 * 24)

        # Total travel time
        total_time_days = 2 * accel_time_days + coasting_time_days

        # Calculate arrival date
        today = datetime.today()
        arrival_date = today + timedelta(days=total_time_days)

        return {
            "total_time_days": round(total_time_days, 1),
            "acceleration_time_days": round(accel_time_days, 1),
            "deceleration_time_days": round(accel_time_days, 1),
            "coasting_time_days": round(coasting_time_days, 1),
            "peak_velocity_km_s": round(peak_velocity_m_s / 1000, 1),
            "sustained_acceleration_g": round(acceleration_m_s2 / self.g, 2),
            "fuel_required_kg": round(self.fuel_mass, 0),
            "arrival_date": arrival_date.strftime("%Y-%m-%d")
        }

# Example Usage:
mission = MissionCalculator(distance_au=0.524, fuel_mass_kg=8000, dry_mass_kg=15500, fuel_type="liquid", sustained_accel=0.2)
result = mission.calculate_mission_time()

# Print results
for key, value in result.items():
    print(f"{key}: {value}")
