import json
from lib.StarType import StarType
from lib.Star import Star
from lib.PlanetType import PlanetType
from lib.Planet import Planet
from lib.EllipticalOrbit import EllipticalOrbit

def load_from_json(config_path):
    with open(config_path, 'r') as file:
        data = json.load(file)

    stars = {star['name']: Star(star['name'], star['mass'], StarType[star['type']], star['AU']) for star in data['stars']}
    planets = []

    for planet_data in data['planets']:
        star = stars[planet_data['orbit']['star']]
        orbit = EllipticalOrbit(
            planet_data['orbit']['eccentricity'],
            planet_data['orbit']['semi_major_axis'],
            planet_data['orbit']['perihelion_day'],
            planet_data['orbit']['perihelion_year'],
            planet_data['orbit']['period'],
            star
        )
        planet = Planet(
            planet_data['name'],
            planet_data['mass'],
            planet_data['radius'],
            PlanetType[planet_data['type']],
            orbit
        )
        planets.append(planet)

    return stars, planets
