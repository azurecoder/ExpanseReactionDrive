from Config import load_from_json
from datetime import datetime, timedelta

if __name__ == "__main__":

    def format_day_of_year(day_of_year, year):
        date = datetime(int(year), 1, 1) + timedelta(days=day_of_year - 1)
        return date.strftime("%d %B")

    stars, planets = load_from_json("./config/solarsystem.json")

    for planet in planets:
        print(f"Details for {planet.name}: ---->")
        closest = planet.get_closest_approach()
        farthest = planet.get_farthest_approach()
        orbital_distance = planet.get_orbital_distance(36.0, 2025)

        print(f"Closest approach to {planet.star.name}: {closest} and in km: {int(round(closest[2] * planet.star.au_in_km, 0)): ,} km")
        print(f"Farthest approach from {planet.star.name}: {farthest} and in km: {int(round(farthest[2] * planet.star.au_in_km, 0)): ,} km")
        print(f"Orbital distance in km on 5th of Feb: {int(round(orbital_distance * planet.star.au_in_km, 0)): ,} km")

    earth = next(planet for planet in planets if planet.name == "Earth")
    mars = next(planet for planet in planets if planet.name == "Mars")
    jupiter = next(planet for planet in planets if planet.name == "Jupiter")

    closest_distance_1, closest_time_1 = earth.find_closest_distance(mars)
    closest_distance_2, closest_time_2 = earth.find_closest_distance(jupiter)
    print(f"Closest distance between Earth and Mars: {int(round(closest_distance_1 * earth.star.au_in_km, 0)): ,} km")
    print(f"Occurs on {format_day_of_year(closest_time_1[0], closest_time_1[1])} of year {int(closest_time_1[1])}")
    print(f"Closest distance between Earth and Jupiter: {int(round(closest_distance_2 * earth.star.au_in_km, 0)): ,} km")
    print(f"Occurs on {format_day_of_year(closest_time_2[0], closest_time_2[1])} of year {int(closest_time_2[1])}")
