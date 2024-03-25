import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 600

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set initial pen color
pen_color = BLACK

# Set initial tool (pen, rectangle, circle, eraser)
tool = "pen"

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Set default font
font = pygame.font.SysFont(None, 30)

# Create a surface for drawing
drawing_surface = pygame.Surface((WIDTH, HEIGHT))
drawing_surface.fill(WHITE)

# Set initial drawing position
start_pos = None

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button pressed
                start_pos = pygame.mouse.get_pos()
            elif event.button == 3:  # Right mouse button pressed
                tool = "eraser"
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button released
                if tool == "rectangle":
                    end_pos = pygame.mouse.get_pos()
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(drawing_surface, pen_color, rect)
                elif tool == "circle":
                    end_pos = pygame.mouse.get_pos()
                    radius = ((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5
                    pygame.draw.circle(drawing_surface, pen_color, start_pos, int(radius))
                start_pos = None
        elif event.type == MOUSEMOTION:
            if start_pos and tool == "pen":  # If left mouse button is held and pen tool is selected
                end_pos = pygame.mouse.get_pos()
                pygame.draw.line(drawing_surface, pen_color, start_pos, end_pos, 5)
                start_pos = end_pos
        elif event.type == KEYDOWN:
            if event.key == K_r:  # Press 'r' for rectangle tool
                tool = "rectangle"
            elif event.key == K_c:  # Press 'c' for circle tool
                tool = "circle"
            elif event.key == K_e:  # Press 'e' for eraser tool
                tool = "eraser"
            elif event.key == K_p:  # Press 'p' for pen tool
                tool = "pen"
            elif event.key == K_1:  # Press '1' for black color
                pen_color = BLACK
            elif event.key == K_2:  # Press '2' for white color
                pen_color = WHITE

    # Clear the screen
    screen.fill(WHITE)

    # Draw the drawing surface on the screen
    screen.blit(drawing_surface, (0, 0))

    # Display current tool and color
    tool_text = font.render("Tool: " + tool.capitalize(), True, BLACK)
    color_text = font.render("Color: " + ("Black" if pen_color == BLACK else "White"), True, BLACK)
    screen.blit(tool_text, (10, 10))
    screen.blit(color_text, (10, 40))

    # Update the display
    pygame.display.update()