import random
import math

class Spark:
    def __init__(self, x, y, r, dx, dy, colour):
        self.x = x
        self.y = y
        self.r = r
        self.dx = dx
        self.dy = dy
        self.colour = colour



def add_sparks(sparks, spark, x, y):    
    colour = generate_spark_colours()  # spark colour generated
    r = 2 #radius
    sparks.append(
        Spark(
            x,
            y, ## snowflake y position start
            r, #radius
            get_final_x(spark, x), # spark final x position
            get_final_y(spark, y), # spark final y position
            colour,
        )
    )

def generate_spark_colours():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return [red, green, blue]

def get_final_x(spark, x):
    radius = 100
    x = radius * math.cos(spark) + x
    print("DX")
    print (x)
    return x

def get_final_y(spark, y):
    radius = 100
    y = radius * math.sin(spark) + y
    print("DY")
    print (y)
    return y


