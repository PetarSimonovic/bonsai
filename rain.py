import random


class Raindrop:
    def __init__(self, x, y, dx, dy, colour):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.colour = colour
        self.width = 2
        self.length = 5



def add_raindrop(raindrops, width, height):    
    r = 1## raindrop radius generated
    colour = random.randint(220, 255) # raindrop colour generated
    raindrops.append(
        Raindrop(
            random.randint(r, r + (width - 2 * r)), ## raindrop x position start
            0, ## raindrop y position start
            (5 - r), # raindrop x speed
            (25 - r), # raindrop y speed
            colour,
        )
    )
    
def fall(raindrop, width, height):
    raindrop.x += raindrop.dx
    raindrop.y += raindrop.dy

    xmax = width - 3 ## these magic numbers refer to values in main.rainfall
    xmin = 3
    ymax = height - 4
    ymin = 4

    if raindrop.x < xmin or raindrop.x > xmax:
        raindrop.x = 0

    if raindrop.y < ymin or raindrop.y > ymax:
        raindrop.y = 0