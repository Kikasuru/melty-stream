from cc_mem import meltyFind, read

import os, sys
import pygame

# Set the working directory to where the script is running.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialise pygame.
pygame.init()
clock = pygame.time.Clock()

from themes.test.__main__ import *

# Set the title and icon.
icon = pygame.image.load("icon.png")
pygame.display.set_caption("Melty-Stream")
pygame.display.set_icon(icon)
del icon

# Create the screen.
screen = pygame.display.set_mode(SCREEN_SIZE)

# Make a find tick variable for later use.
LOOK_TIC_MAX = 60
meltyLookTic = LOOK_TIC_MAX

while True:
    # Close the window when asked for.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # If the header for Melty does not exist, try to find Melty Blood.
    if read(0x400000) == None:
        # Check if the look tic equals 0.
        if meltyLookTic == 0:
            # Look for Melty
            meltyFind()
            # Reset the look tic.
            meltyLookTic = LOOK_TIC_MAX
        else:
            # Count the look tic down.
            meltyLookTic -= 1

    # Render the screen.
    screen.blit(render(read(0x400000)), (0,0))
    pygame.display.flip()

    # Keep it at 60 fps.
    clock.tick(60)
