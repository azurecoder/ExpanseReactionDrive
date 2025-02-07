import sys
import pygame
from lib import PlanetType, EllipticalOrbit, Planet
import Config as cf

stars, planets = cf.load_from_json("./config/solarsystem.json")
mercury = [p for p in planets if p.name == "Mercury"][0].get_farthest_approach()[2] * 1 
venus = [p for p in planets if p.name == "Venus"][0].get_farthest_approach()[2] * 2 
earth = [p for p in planets if p.name == "Earth"][0].get_farthest_approach()[2] * 3 
mars = [p for p in planets if p.name == "Mars"][0].get_farthest_approach()[2] * 4 
jupiter = [p for p in planets if p.name == "Jupiter"][0].get_farthest_approach()[2] * 5 
saturn = [p for p in planets if p.name == "Saturn"][0].get_farthest_approach()[2] * 6 
uranus = [p for p in planets if p.name == "Uranus"][0].get_farthest_approach()[2] * 7 
neptune = [p for p in planets if p.name == "Neptune"][0].get_farthest_approach()[2] * 8 
mercury = (mercury / neptune) * 580
venus = (venus / neptune) * 580
earth = (earth / neptune) * 580
mars = (mars / neptune) * 580   
jupiter = (jupiter / neptune) * 580
saturn = (saturn / neptune) * 580
uranus = (uranus / neptune) * 580
neptune = (neptune / neptune) * 580

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
print(planets)
"""
# Initialize pygame
pygame.init()

# Set up display
width, height = 1200, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Canvas with Yellow Circle")

# Define colors
yellow = (255, 255, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# Circle properties
circle_radius = 5
circle_pos = (width // 2, height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    pygame.draw.circle(screen, yellow, circle_pos, circle_radius)
    for i, p in enumerate(planets):
        pygame.draw.circle(screen, green, (int(width // 2 + p), height // 2), 5)
    pygame.display.flip()

pygame.quit()
sys.exit()
"""