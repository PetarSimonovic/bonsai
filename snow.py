import random


class Snowflake:
    def __init__(self, x, y, r, dx, dy, colour):
        self.x = x
        self.y = y
        self.r = r
        self.dx = dx
        self.dy = dy
        self.colour = colour



def add_snowflake(snowflakes, width, height):    
    r = random.randint(0, 2) + 1 # snowflake radius generated
    colour = random.randint(220, 255) # snowflake colour generated
    snowflakes.append(
        Snowflake(
            random.randint(r, r + (width - 2 * r)), ## snowflake x position start
            0, ## snowflake y position start
            r,
            (14 - r) / 3, # snowflake x speed
            (14 - r) / 3, # snowflake y speed
            colour,
        )
    )
    
def fall(snowflake, width, height):
    snowflake.x += snowflake.dx
    snowflake.y += snowflake.dy

    xmax = width - snowflake.r
    xmin = snowflake.r
    ymax = height - snowflake.r
    ymin = snowflake.r

    if snowflake.x < xmin or snowflake.x > xmax:
        snowflake.x = 0

    if snowflake.y < ymin or snowflake.y > ymax:
        snowflake.y = 0

