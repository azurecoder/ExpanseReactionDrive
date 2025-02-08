import sys
import pygame
from lib import PlanetType, EllipticalOrbit, Planet
import Config as cf

screen_radius = 1130
planet_radius = 14

stars, planets = cf.load_from_json("./config/solarsystem.json")
mercury = [p for p in planets if p.name == "Mercury"][0].get_farthest_approach()[2] * 1 
venus = [p for p in planets if p.name == "Venus"][0].get_farthest_approach()[2] * 2 
earth = [p for p in planets if p.name == "Earth"][0].get_farthest_approach()[2] * 3 
mars = [p for p in planets if p.name == "Mars"][0].get_farthest_approach()[2] * 4 
jupiter = [p for p in planets if p.name == "Jupiter"][0].get_farthest_approach()[2] * 5 
saturn = [p for p in planets if p.name == "Saturn"][0].get_farthest_approach()[2] * 6 
uranus = [p for p in planets if p.name == "Uranus"][0].get_farthest_approach()[2] * 7 
neptune = [p for p in planets if p.name == "Neptune"][0].get_farthest_approach()[2] * 8 
mercury = (mercury / neptune) * screen_radius
venus = (venus / neptune) * screen_radius
earth = (earth / neptune) * screen_radius
mars = (mars / neptune) * screen_radius
jupiter = (jupiter / neptune) * screen_radius
saturn = (saturn / neptune) * screen_radius
uranus = (uranus / neptune) * screen_radius
neptune = (neptune / neptune) * screen_radius

planet_radius_constant = (planet_radius-2) / [p for p in planets if p.name == "Jupiter"][0].radius

planets_distances = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
colours = [(139, 69, 19), (120, 60, 59), (101, 51, 99), (83, 42, 139), (64, 32, 179), (45, 23, 219), (27, 14, 239), (0, 0, 255)]
plant_radii = [p.radius * (planet_radius_constant+2) for p in planets]

icons = [f"./media/{p.name.lower()}.png" for p in planets]

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
circle_radius = 10
# circle_pos = (width // 2, height // 2)
circle_pos = (0, height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    pygame.draw.circle(screen, yellow, circle_pos, circle_radius)
    
    planet_images = [pygame.transform.scale(pygame.image.load(icon), (int(plant_radii[i] * 2), int(plant_radii[i] * 2)))
                     for i, icon in enumerate(icons)]
    for i, p in enumerate(planets_distances):
        screen.blit(planet_images[i], (p + (circle_radius + 5) - plant_radii[i], height // 2 - plant_radii[i]))
        # Display tooltips when hovering over planet images
        mouse_pos = pygame.mouse.get_pos()
        font = pygame.font.SysFont(None, 24)
        for i, distance in enumerate(planets_distances):
            x = distance + (circle_radius + 5) - plant_radii[i]
            y = height // 2 - plant_radii[i]
            rect = pygame.Rect(x, y, int(plant_radii[i] * 2), int(plant_radii[i] * 2))
            if rect.collidepoint(mouse_pos):
                tooltip_surface = font.render(f"{planets[i].name} [{planets[i].get_farthest_approach()[2]:.2f} AU]", True, green)
                tooltip_rect = tooltip_surface.get_rect()
                pos_x = mouse_pos[0] + 10
                tooltip_rect.topleft = (pos_x, mouse_pos[1] + 10)
                if planets[i].name == "Neptune":
                    mouse_pos = (mouse_pos[0] - 110, mouse_pos[1])
                tooltip_rect = tooltip_surface.get_rect()
                tooltip_rect.topleft = (mouse_pos[0] + 10, mouse_pos[1] + 10)
                screen.blit(tooltip_surface, tooltip_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()