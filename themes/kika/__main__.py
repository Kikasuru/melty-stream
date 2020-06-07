import pygame
import math
from cc_mem import read
from locals.cc_mem import *
from locals.cc_char import getCharName

# Set Constants.
SCREEN_SIZE = width, height = 270,1080
ANIM_MAX    = 1000
ANIM_MIN    = 0
ANIM_SPEED  = ANIM_MAX / 20
ANIM_SPEED2 = ANIM_MAX / 16
ANIM_ALPHA = -5
P1_BORDER_POSX = 0
P2_BORDER_POSX = 1710

# Make variables for the rendering process.
p1LastChar = None
p1LastMoon = None
p1LastClor = None
p1LastMode = 0
p1Surface = pygame.Surface((270,1080))
p1NameSurface = None
p1CharSurface = None
p1Cha2Surface = None
p1MoonSurface = None
p1ClorSurface = None
p1SelectAnim = ANIM_MIN
p1SelectAni2 = ANIM_MIN
p1SelectAnimStart = False
p1SelectAnimType = ANIM_MAX

def colorBorder(color):
    # Make a surface for this border.
    borderSurface = pygame.Surface((270,1080), pygame.SRCALPHA)

    # Draw a bacground for a circle.
    pygame.draw.circle(borderSurface, [0,1,8], (227,1037), 48)
    # Draw a circle in the corner.
    pygame.draw.circle(borderSurface, color, (227,1037), 48, 5)
    # Mask out it's bottom left corner.
    pygame.draw.rect(borderSurface, [0,1,8], pygame.Rect(227,1037,48,48))

    # Make a line going up.
    pygame.draw.line(borderSurface, color, (267,1017), (267,0), 5)
    # Make a line going to the left.
    pygame.draw.line(borderSurface, color, (206,1077), (0,1077), 5)

    # Return the surface.
    return borderSurface

def render(game):
    global p1LastChar,p1LastMoon,p1LastClor,p1LastMode
    global p1Surface,p1NameSurface,p1CharSurface,p1Cha2Surface,p1MoonSurface,p1ClorSurface
    global p1SelectAnim,p1SelectAni2,p1SelectAnimStart,p1SelectAnimType

    # Fill the background for Player 1's border.
    p1Surface.fill([0,1,8])

    if game:
        # Check if Player 1 has changed their character.
        if read(CC_P1_CHARACTER_ADDR)[0] != p1LastChar:
            # Load the name of the character and rotate it.
            oldNameSurf = pygame.image.load("themes/kika/assets/name/vs_name00_"+str(read(CC_P1_CHARACTER_ADDR)[0]).zfill(2)+".png")
            p1NameSurface = pygame.transform.rotate(oldNameSurf, 90)

            # If the character is not a random character.
            if read(CC_P1_CHARACTER_ADDR)[0] != 0x63:
                # Load the character image.
                p1CharSurface = pygame.image.load("themes/kika/assets/mug0/cut_"+str(read(CC_P1_CHARACTER_ADDR)[0]).zfill(2)+"00.png")

                # If the character is a duo, load the second character.
                if read(CC_P1_CHARACTER_ADDR)[0] in (0x04, 0x22, 0x23):
                    p1Cha2Surface = pygame.image.load("themes/kika/assets/mug0/cut_"+str(read(CC_P1_CHARACTER_ADDR)[0]).zfill(2)+"01.png")

            # Load the character's color palettes.
            p1ClorSurface = pygame.image.load("themes/kika/assets/color/color_c"+str(read(CC_P1_CHARACTER_ADDR)[0]).zfill(2)+".png")

            # Set the last character.
            p1LastChar = read(CC_P1_CHARACTER_ADDR)[0]

            # Turn the animation off immediately.
            p1SelectAnim = ANIM_MIN
            p1SelectAni2 = ANIM_MIN
            p1SelectAnimStart = False
            p1SelectAnimType = ANIM_MAX

        # Check if a character has been selected.
        if read(CC_P1_SELECTOR_MODE_ADDR)[0] == 1 and p1LastMode != 1:
            # Start the Animation.
            p1SelectAnim = ANIM_MIN
            p1SelectAni2 = ANIM_MIN
            p1SelectAnimStart = True
            p1SelectAnimType = ANIM_MAX

            # Set the last mode.
            p1LastMode = read(CC_P1_SELECTOR_MODE_ADDR)[0]

        # Check if a character has been deselected.
        if read(CC_P1_SELECTOR_MODE_ADDR)[0] == 0 and p1LastMode != 0:
            # Start the Animation.
            p1SelectAnim = ANIM_MAX
            p1SelectAni2 = ANIM_MAX
            p1SelectAnimStart = True
            p1SelectAnimType = ANIM_MIN

            # Set the last mode.
            p1LastMode = read(CC_P1_SELECTOR_MODE_ADDR)[0]

        # Check if the animation is still going, and increase it if so.
        if p1SelectAnimStart:
            if p1SelectAnimType == ANIM_MAX:
                p1SelectAnim += ANIM_SPEED
                p1SelectAni2 += ANIM_SPEED2
            else:
                p1SelectAnim -= ANIM_SPEED
                p1SelectAni2 -= ANIM_SPEED2
            # Check if the animation is finished.
            if p1SelectAnim == p1SelectAnimType:
                # If so, end the animation.
                p1SelectAnim = p1SelectAnimType
                p1SelectAni2 = p1SelectAnimType
                p1SelectAnimStart = False

        # Render the character.
        yanim = (p1CharSurface.get_width() * -1) + p1CharSurface.get_width() * (1 - math.exp((p1SelectAnim / ANIM_MAX) * ANIM_ALPHA))
        p1Surface.blit(p1CharSurface, (yanim,56))

        # If the character is a duo, render their partner.
        if read(CC_P1_CHARACTER_ADDR)[0] in (0x04, 0x22, 0x23):
            yanim = (p1Cha2Surface.get_width() * -1) + p1Cha2Surface.get_width() * (1 - math.exp((p1SelectAni2 / ANIM_MAX) * ANIM_ALPHA))
            p1Surface.blit(p1Cha2Surface, (yanim,56))

        # Draw the name of the character.
        p1Surface.blit(p1NameSurface, (222,0))

        # Grab the currently selected color.
        colorx = 1 + ((read(CC_P1_COLOR_SELECTOR_ADDR)[0] % 8) * 32)
        colory = 3 + (math.floor(read(CC_P1_COLOR_SELECTOR_ADDR)[0] / 8) * 16)
        color  = p1ClorSurface.get_at((colorx,colory))
        # Draw the color border.
        p1Surface.blit(colorBorder(color),(0,0))

    # Return P1 Surface.
    return p1Surface
