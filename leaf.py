import random


class Leaf:
    def __init__(self, x, y, r, colour):
        self.x = x
        self.y = y
        self.r = r
        self.colour = colour



def add_leaf(leaves, branchX, branchY):    
    r = random.uniform(1.0, 2.0) + 0.3 # leaf radius generated
    colour = autumn_colours() # leaf colour generated
    leaves.append(
        Leaf(
            branchX, ## snowflake x position start
            branchY, ## snowflake y position start
            r,
            colour,
        )
        )
    
def spring_colours():
    colours = [
        [170, 213, 118],
        [115, 169, 66],
        [83, 141, 34]
        ]
    return random.choice(colours)

def autumn_colours():
    colours = [
        [220, 47, 2],
        [232, 93, 4],
        [244, 140, 6]
        ]
    return random.choice(colours)



