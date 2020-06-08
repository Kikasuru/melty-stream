import pygame
from cc_mem import read
from locals.cc_mem import *
from locals.cc_char import getCharName

# Set Constants.
SCREEN_SIZE = width, height = 160, 240

# Make a new surface.
surface = pygame.Surface(SCREEN_SIZE)

# Create a debug font.
sm_font = pygame.font.Font("./themes/test/assets/04B_11__.TTF", 8)

def render(game):
    global surface

    # Fill the surface with black.
    surface.fill([0,0,0])

    # Make a debug text renderer.
    def renderText(text,pos):
        surface.blit(sm_font.render(text, False, [255,255,255]), pos)

    if game:
        # Print debug text.
        renderText(str(read(CC_P1_SELECTOR_MODE_ADDR)[0]),(0,0))
        renderText(getCharName(read(CC_P1_CHARACTER_ADDR)[0]),(0,8))
        renderText(str(read(CC_P1_MOON_SELECTOR_ADDR)[0]),(0,16))
        renderText(str(read(CC_P1_COLOR_SELECTOR_ADDR)[0]),(0,24))

        renderText(str(read(CC_P2_SELECTOR_MODE_ADDR)[0]),(0,40))
        renderText(getCharName(read(CC_P2_CHARACTER_ADDR)[0]),(0,48))
        renderText(str(read(CC_P2_MOON_SELECTOR_ADDR)[0]),(0,56))
        renderText(str(read(CC_P2_COLOR_SELECTOR_ADDR)[0]),(0,64))

        renderText(str(read(CC_STAGE_SELECTOR_ADDR)[0]),(0,80))
    else:
        renderText("Waiting...",(0,0))

    # Return the surface.
    return surface
