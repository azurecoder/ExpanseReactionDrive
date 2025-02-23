import sys

import pygame
from lib import PlanetType, EllipticalOrbit, Planet
import Config as cf

# New variables and constants for the destination click behavior
AU_TO_KM = 149597870.7
final_tooltip_text = None

# Persistent state for planet selections
selected_planet_index = None
destination_planet_index = None
drag_start_x = None
drag_line_y = None

screen_radius = 1130
planet_radius = 14

# Define the Clear button drawing and event handling functions
def draw_clear_button(surface):
    button_rect = pygame.Rect(surface.get_width() - 110, 10, 100, 40)
    pygame.draw.rect(surface, (200, 200, 200), button_rect)
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render("Clear", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=button_rect.center)
    surface.blit(text_surface, text_rect)
    return button_rect

def handle_clear_button_event(event, button_rect):
    global selected_planet_index, destination_planet_index, drag_start_x, drag_line_y
    if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
        selected_planet_index = None
        destination_planet_index = None
        drag_start_x = None
        drag_line_y = None

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
# button_rect will be computed each frame
# Main loop
running = True
while running:
    button_rect = pygame.Rect(screen.get_width() - 110, 10, 100, 40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        handle_clear_button_event(event, button_rect)
    screen.fill(black)
    button_rect = draw_clear_button(screen)
    pygame.draw.circle(screen, yellow, circle_pos, circle_radius)
    pygame.draw.circle(screen, yellow, circle_pos, circle_radius)
    
    # First, draw all planet images and store their positions
    planet_images = [pygame.transform.scale(pygame.image.load(icon), (int(plant_radii[i] * 2), int(plant_radii[i] * 2)))
                     for i, icon in enumerate(icons)]
    planet_positions = []
    for i, distance in enumerate(planets_distances):
        x = distance + (circle_radius + 5) - plant_radii[i]
        y = height // 2 - plant_radii[i]
        planet_positions.append((x, y))
        screen.blit(planet_images[i], (x, y))

    mouse_pos = pygame.mouse.get_pos()
    font = pygame.font.SysFont(None, 24)
    for i, (x, y) in enumerate(planet_positions):
        rect = pygame.Rect(x, y, int(plant_radii[i] * 2), int(plant_radii[i] * 2))
        if rect.collidepoint(mouse_pos):
            tooltip_surface = font.render(f"{planets[i].name} [{planets[i].get_farthest_approach()[2]:.2f} AU]", True, green)
            tooltip_rect = tooltip_surface.get_rect()
            #if planets[i].name == "Neptune":
            #    mouse_pos = (mouse_pos[0] - 110, mouse_pos[1])
            tooltip_rect.topleft = (mouse_pos[0] + 10, mouse_pos[1] + 10)
            screen.blit(tooltip_surface, tooltip_rect)
            mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            if rect.collidepoint(mouse_pos):
                if selected_planet_index is None:
                    selected_planet_index = i
                    drag_start_x = mouse_pos[0]
                    drag_line_y = y + plant_radii[i]
                elif selected_planet_index is not None and selected_planet_index != i:
                    destination_planet_index = i
                    distance_val = abs(planets_distances[selected_planet_index] - planets_distances[destination_planet_index])
                    tooltip_text = f"{planets[selected_planet_index].name} -> {planets[i].name}: {distance_val:.2f} AU"
                    tooltip_surface = font.render(tooltip_text, True, green)
                    screen.blit(tooltip_surface, (mouse_pos[0] + 10, mouse_pos[1] + 10))
        # Always keep the red circle overlays on the selected and destination planets
        if selected_planet_index == i:
            pygame.draw.circle(screen, (255, 0, 0), (x + plant_radii[i], y + plant_radii[i]), 6, 0)
        if destination_planet_index == i:
            pygame.draw.circle(screen, (255, 0, 0), (x + plant_radii[i], y + plant_radii[i]), 6, 0)

    # Draw the red line: if a planet is selected, always draw the red line.
    if selected_planet_index is not None and drag_start_x is not None:
        if destination_planet_index is None:
            # line follows the mouse position
            current_x = pygame.mouse.get_pos()[0]
            end_x = current_x
        else:
            # line points to the center of the destination planet
            dest_x, dest_y = planet_positions[destination_planet_index]
            end_x = dest_x + plant_radii[destination_planet_index]
        pygame.draw.line(screen, (255, 0, 0), (drag_start_x, drag_line_y), (end_x, drag_line_y), 2)
        
        # If destination planet is selected, add distance text in white at the middle of the red line.
        if destination_planet_index is not None:
            # Calculate the closest distance in AU, convert to km using AU_TO_KM.
            distance_au = planets[selected_planet_index].find_closest_distance(planets[destination_planet_index])
            distance_km = int(distance_au[0]) * AU_TO_KM
            distance_text = f"{distance_km:,.0f} km"
            text_surface = font.render(distance_text, True, (255, 255, 255))
            mid_x = (drag_start_x + end_x) // 2
            mid_y = drag_line_y - text_surface.get_height() - 5
            screen.blit(text_surface, (mid_x, mid_y))

    pygame.display.flip()

pygame.quit()
sys.exit()