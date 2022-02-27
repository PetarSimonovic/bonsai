import random


class Spark:
    def __init__(self, x, y, r, dx, dy, colour):
        self.x = x
        self.y = y
        self.r = r
        self.dx = dx
        self.dy = dy
        self.colour = colour



def add_sparks(sparks, x, y):    
    colour = generate_spark_colours()  # spark colour generated
    r = 0.6 #radius
    sparks.append(
        Spark(
            x,
            y, ## snowflake y position start
            r, #radius
            (14 - r) / 3, # spark x speed
            (14 - r) / 3, # spark y speed
            colour,
        )
    )

def generate_spark_colours():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return [red, green, blue] 
    
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


