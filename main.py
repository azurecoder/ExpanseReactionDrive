from Config import load_from_json

if __name__ == "__main__":
    stars, planets = load_from_json("./config/solarsystem.json")

    for planet in planets:
        print(f"Details for {planet.name}: ---->")
        closest = planet.get_closest_approach()
        farthest = planet.get_farthest_approach()
        orbital_distance = planet.get_orbital_distance(36.0, 2025)

        print(f"Closest approach to {planet.star.name}: {closest} and in km: {int(round(closest[2] * planet.star.au_in_km, 0)): ,} km")
        print(f"Farthest approach from {planet.star.name}: {farthest} and in km: {int(round(farthest[2] * planet.star.au_in_km, 0)): ,} km")
        print(f"Orbital distance in km on 5th of Feb: {int(round(orbital_distance * planet.star.au_in_km, 0)): ,} km")
