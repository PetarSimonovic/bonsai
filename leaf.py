import random


class Leaf:
    def __init__(self, x, y, r, colour):
        self.x = x
        self.y = y
        self.r = r
        self.colour = colour



def add_leaf(leaves, season, branchX, branchY):
    r = get_leaf_size(season) # leaf radius generated
    colour = season_colours(season) # leaf colour generated
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
        [244, 140, 6],
        [250, 63, 7],
        [255, 186, 8]
        ]
    return random.choice(colours)

def season_colours(season):
    if season == "spring" or season == "summer" :
        return spring_colours()
    else:
        return autumn_colours()

def get_leaf_size(season):
    if season == "spring":
        return random.uniform(0.5, 0.8) + 0.5
    else:
        return random.uniform(1, 2) + 1

