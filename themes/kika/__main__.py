import pygame
import math
from cc_mem import read
from locals.cc_mem import *
from locals.cc_char import getCharName

# Set Constants.
SCREEN_SIZE     = width, height = 1920,1080
ANIM_MAX        = 1000
ANIM_MIN        = 0
ANIM_SPEED      = ANIM_MAX / 20
ANIM_SPEED2     = ANIM_MAX / 16
ANIM_ALPHA      = -5
P1_BORDER_POSX  = 0
P2_BORDER_POSX  = 1710

# Make variables for the rendering process.
Surface       = pygame.Surface((1920,1080))

LastChar      = [None,None]
LastMode      = [0,0]
NameSurface   = [None,None]
CharSurface   = [None,None]
Cha2Surface   = [None,None]
MoonSurface   = [None,None]
MoGlSurface   = [None,None]
ClorSurface   = [None,None]

SelectAnim        = [ANIM_MIN,ANIM_MIN]
SelectAni2        = [ANIM_MIN,ANIM_MIN]
SelectAnimStart   = [False,False]
SelectAnimType    = [ANIM_MAX,ANIM_MAX]

MoonAnim          = [ANIM_MIN,ANIM_MIN]
MoonAnimStart     = [False,False]


def colorRender(color):
    # Make a surface for this border.
    colorSurface = pygame.Surface((270,1080), pygame.SRCALPHA)

    # Draw a bacground for a circle.
<<<<<<< HEAD
    pygame.draw.circle(colorSurface, [0,1,8], (215,1025), 56)
    # Draw a circle in the corner.
    pygame.draw.circle(colorSurface, color, (215,1025), 56, 5)
    # Mask out it's bottom left corner.
    pygame.draw.rect(colorSurface, [0,1,8], pygame.Rect(215,1025,56,56))

    # Make a line going up.
    pygame.draw.line(colorSurface, color, (267,1017), (267,0), 5)
    # Make a line going to the left.
    pygame.draw.line(colorSurface, color, (206,1077), (0,1077), 5)
=======
    pygame.draw.circle(borderSurface, [0,1,8], (227,1037), 48)
    # Draw a circle in the corner.
    pygame.draw.circle(borderSurface, color, (227,1037), 48, 5)
    # Mask out it's bottom left corner.
    pygame.draw.rect(borderSurface, [0,1,8], pygame.Rect(227,1037,48,48))

    # Make a line going up.
    pygame.draw.line(borderSurface, color, (267,1017), (267,0), 5)
    # Make a line going to the left.
    pygame.draw.line(borderSurface, color, (206,1077), (0,1077), 5)
>>>>>>> 1faf8b299a8a9dd4cf170ca6d1852434dcdc8314

    # Return the surface.
    return colorSurface

def borderRender(i):
    global LastChar,LastMoon,LastClor,LastMode
    global Surface,NameSurface,CharSurface,Cha2Surface,MoonSurface,MoGlSurface,ClorSurface
    global SelectAnim,SelectAni2,SelectAnimStart,SelectAnimType
    global MoonAnim,MoonAnimStart

    # Create a surface.
    BorderSurface = pygame.Surface((270,1080))

    # Fill the background for this player's border.
    BorderSurface.fill([0,1,8])

    # Set some bytes for the player this border belongs to.
    if i == 0:
        CC_SELECTOR_MODE = read(CC_P1_SELECTOR_MODE_ADDR)[0]
        CC_CHARACTER = read(CC_P1_CHARACTER_ADDR)[0]
        CC_MOON_SELECTOR = read(CC_P1_MOON_SELECTOR_ADDR)[0]
        CC_COLOR_SELECTOR = read(CC_P1_COLOR_SELECTOR_ADDR)[0]
    if i == 1:
        CC_SELECTOR_MODE = read(CC_P2_SELECTOR_MODE_ADDR)[0]
        CC_CHARACTER = read(CC_P2_CHARACTER_ADDR)[0]
        CC_MOON_SELECTOR = read(CC_P2_MOON_SELECTOR_ADDR)[0]
        CC_COLOR_SELECTOR = read(CC_P2_COLOR_SELECTOR_ADDR)[0]

    # Check if Player 1 has changed their character.
    if CC_CHARACTER != LastChar[i]:
        # Load the name of the character and rotate it.
        oldNameSurf = pygame.image.load("themes/kika/assets/name/vs_name00_"+str(CC_CHARACTER).zfill(2)+".png")
        NameSurface[i] = pygame.transform.rotate(oldNameSurf, 90)
        # If this is the 2nd player's border, flip the name.
        if i == 1: NameSurface[i] = pygame.transform.flip(NameSurface[i], True, False)

        # If the character is not a random character.
        if CC_CHARACTER != 0x63:
            # Load the character image.
            CharSurface[i] = pygame.image.load("themes/kika/assets/mug0/cut_"+str(CC_CHARACTER).zfill(2)+"00.png")

            # If the character is a duo, load the second character.
            if CC_CHARACTER in (0x04, 0x22, 0x23):
                Cha2Surface[i] = pygame.image.load("themes/kika/assets/mug0/cut_"+str(CC_CHARACTER).zfill(2)+"01.png")

        # Load the character's color palettes.
        ClorSurface[i] = pygame.image.load("themes/kika/assets/color/color_c"+str(CC_CHARACTER).zfill(2)+".png")

        # Set the last character.
        LastChar[i] = CC_CHARACTER

        # Turn the animation off immediately.
        SelectAnim[i] = ANIM_MIN
        SelectAni2[i] = ANIM_MIN
        SelectAnimStart[i] = False
        SelectAnimType[i] = ANIM_MAX

    # Check if a character has been selected.
    if CC_SELECTOR_MODE == 1 and LastMode[i] != 1:
        # Start the Animation.
        SelectAnim[i] = ANIM_MIN
        SelectAni2[i] = ANIM_MIN
        SelectAnimStart[i] = True
        SelectAnimType[i] = ANIM_MAX

    # Check if a character has been deselected.
    if CC_SELECTOR_MODE == 0 and LastMode[i] != 0:
        # Start the Animation.
        SelectAnim[i] = ANIM_MAX
        SelectAni2[i] = ANIM_MAX
        SelectAnimStart[i] = True
        SelectAnimType[i] = ANIM_MIN

    # Check if the animation is still going, and increase it if so.
    if SelectAnimStart[i]:
        if SelectAnimType[i] == ANIM_MAX:
            SelectAnim[i] += ANIM_SPEED
            SelectAni2[i] += ANIM_SPEED2
        else:
            SelectAnim[i] -= ANIM_SPEED
            SelectAni2[i] -= ANIM_SPEED2
        # Check if the animation is finished.
        if SelectAnim[i] == SelectAnimType[i]:
            # If so, end the animation.
            SelectAnim[i] = SelectAnimType[i]
            SelectAni2[i] = SelectAnimType[i]
            SelectAnimStart[i] = False

    # Render the character.
    yanim = (CharSurface[i].get_width() * -1) + CharSurface[i].get_width() * (1 - math.exp((SelectAnim[i] / ANIM_MAX) * ANIM_ALPHA))
    BorderSurface.blit(CharSurface[i], (yanim,56))

    # If the character is a duo, render their partner.
    if CC_CHARACTER in (0x04, 0x22, 0x23):
        yanim = (Cha2Surface[i].get_width() * -1) + Cha2Surface[i].get_width() * (1 - math.exp((SelectAni2[i] / ANIM_MAX) * ANIM_ALPHA))
        BorderSurface.blit(Cha2Surface[i], (yanim,56))

    # Draw the name of the character.
    BorderSurface.blit(NameSurface[i], (222,0))

    # Grab the currently selected color.
    colorx = 1 + ((CC_COLOR_SELECTOR % 8) * 32)
    colory = 3 + (math.floor(CC_COLOR_SELECTOR / 8) * 16)
    color  = ClorSurface[i].get_at((colorx,colory))
    # Draw the color border.
    BorderSurface.blit(colorRender(color),(0,0))

    # Check if a moon has been selected.
    if CC_SELECTOR_MODE == 2 and LastMode != 2:
        # Load the moon's graphics.
        MoonSurface[i] = pygame.image.load("themes/kika/assets/moon/moon_"+str(CC_MOON_SELECTOR)+".png")
        MoGlSurface[i] = pygame.image.load("themes/kika/assets/moon/moon_"+str(CC_MOON_SELECTOR)+"g.png")
        MoGlSurface[i].set_alpha(None)

        # Start the Animation.
        MoonAnim[i] = ANIM_MAX
        MoonAnimStart[i] = True

    # Check if a moon has been deselected.
    print(LastMode[i])
    if CC_SELECTOR_MODE < 2 and LastMode[i] >= 2:
        # Turn the animation off immediately.
        MoonAnim[i] = ANIM_MIN
        MoonAnimStart[i] = False

    # Check if the animation is still going, and decrease it if so.
    #if MoonAnimStart[i]:
    #    MoonAnim[i] -= ANIM_SPEED
    #    # Check if the animation is finished.
    #    if MoonAnim[i] == ANIM_MIN:
    #        # If so, end the animation.
    #        MoonAnim[i] = ANIM_MIN
    #        MoonAnimStart[i] = False

    # Check if a moon should be displayed
    if CC_SELECTOR_MODE >= 2:
        # Display the moon.
        BorderSurface.blit(MoonSurface[i], (167,977))

        # Set the transparency of the moon's glow.
        #MoGlSurface[i].set_alpha(int(round(MoonAnim[i] / ANIM_MAX)*255))
        # Display the moon's glow.
        #Surface.blit(MoGlSurface, (159,969))

    # If the last mode is different from the one ingame, change it.
    if CC_SELECTOR_MODE != LastMode[i]:
        LastMode[i] = CC_SELECTOR_MODE

    # Return the border surface.
    return BorderSurface

def render(game):
    # Fill the background for the surface.
    Surface.fill([0,255,0])

    if game:
        # Render both player's borders, flipping player 2's.
        p1Border = borderRender(0)
        p2Border = pygame.transform.flip(borderRender(1), True, False)

        # Blit them onto the surface.
        Surface.blit(p1Border, (P1_BORDER_POSX, 0))
        Surface.blit(p2Border, (P2_BORDER_POSX, 0))

    # Return the surface.
    return Surface
