'''
Menú de inicio para iniciar la animación de la soluicón óptima del problema
How to Cross the River: donde el granjero debe cruzar el río con un zorro, un ganso y un saco de maíz;
hecho con Pygame.
'''

# Required libraries
import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set the screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption('How to Cross the River')

# Set the background color
WHITE = (255, 255, 255)
screen.fill(WHITE)

# Set the font
font = pygame.font.Font(None, 36)

# Set the text
text = font.render('Press any key to start the animation', True, (0, 0, 0))

# Set the text position
text_rect = text.get_rect()
text_rect.center = (WIDTH // 2, HEIGHT // 2)

# Set the animation speed
clock = pygame.time.Clock()

# Set the animation status
running = False

# Main loop
def main():
    global running
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                running = True
        if running:
            break
        screen.fill(WHITE)
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(60)
        
main()