# SUMMARY OF WHAT'S HAPPENING
import math
import pygame
import colorsys

pygame.init()

# 3 colors
white = (255, 255, 255)  # donut
black = (0, 0, 0)  # background
hue = 1

# setting pygame window size
WIDTH = 1080
HEIGHT = 720

# ----------------------------------------------------------------------------------------------------------------

x_start, y_start = 0, 0  # left top corner starting position

# space between chars
x_separator = 10
y_separator = 20

# rows, columns, and screen size
rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

# D O N U T _ C R E A T I O N

# drawing donut in middle of the screen
x_offset = columns / 2
y_offset = rows / 2

# rotation animation
A, B = 0, 0

# creating donut white
theta_spacing = 10  # density of primary cirle
# donut density amonst primary circle 360° (for faster rotation, change to 2 or 3)
phi_spacing = 1

# chars for illuminate index
chars = ".,-~:;=!*#$@"
# inverted_chars = "@$#*!=;:~-,."


# ---------------------------------------------------------------------------------------------------------------

# screen for pygame window, size of screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

# or if you choose to use fullscreen -- uncomment to use
# display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# caption and font
pygame.display.set_caption('Spinning Donut')
font = pygame.font.SysFont('Inter', 18, bold=True)


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

# displays pygame text


def text_display(letter, x_space, y_space):
    """
    This is a display function
    need parameters for characters and coordinates on screen
    """
    # text = font.render(str(letter), True, white) # black and white
    text = font.render(str(letter), True, hsv2rgb(hue, 0, 1))  # color
    # bleed text on pygame surface
    display_surface.blit(text, (x_start, y_start))

# ---------------------------------------------------------------------------------------------------------------


# pygame runs in a while loop
run = True
while run:

    # start
    screen.fill(black)

    # spinning donut
    z = [0] * screen_size  # fills donut space
    b = [' '] * screen_size  # fills background/'empty' space

    for j in range(0, 628, theta_spacing):  # from 0 to 2π (full circle)
        for i in range(0, 628, phi_spacing):  # also from 0 to 2π (full circle)
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)

            t = c * h * g - f * e

            # 3D x coordinate after rotation
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            # 3D y coordinate after rotation
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + columns * y)  # 3D z coordinate after rotation
            N = int(8 * ((f * e - c * d * g) * m - c * d * e -
                    f * g - l * d * n))  # luminance index w chars

            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_separator - y_separator:
        y_start = 0

    for i in range(len(b)):
        A += 0.00003  # for faster rotation, change to larger value
        B += 0.00002  # for faster rotation, change to larger value
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator

    pygame.display.update()

    # close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
