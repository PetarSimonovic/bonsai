import random
import math

class Spark:
    def __init__(self, x, y, r, colour):
        self.x = x
        self.y = y
        self.r = r
        self.colour = colour



def add_sparks(sparks, spark, x, y):    
    colour = generate_spark_colours()  # spark colour generated
    r = 2 #radius
    sparks.append(
        Spark(
            x,
            y, ## snowflake y position start
            r, #radius
            colour,
        )
    )

def generate_spark_colours():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return [red, green, blue]

def get_x(spark, blast_radius, x):
    x = blast_radius * math.cos(spark) + x
    return x

def get_y(spark, blast_radius, y):
    y = blast_radius * math.sin(spark) + y
    return y


