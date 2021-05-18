import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT, 
)
pygame.init()

#scoring
score = if
# Set up window
screen = pygame.display.set_mode([500,500])

# fill the background with white
screen.fill((255, 255, 255))

# Draw a blue circle in the center
pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

# Flip the display
pygame.display.flip()

# Run until user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit
pygame.quit()
