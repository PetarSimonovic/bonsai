import leaf
import random

class Tree:
    
    
    def __init__(self, display, width, height):
        self.leaves = []
        self.display = display
        self.width = width
        self.height = height
        self.trunk_colour = display.create_pen(118, 82, 46)
        print("Tree here")
        print(self.display)
        
    def draw_trunk(self):
        self.display.rectangle(115, 180, 10, 30) ## x, y, width, height
        self.display.rectangle(113, 200, 13, 15)
        self.display.rectangle(115, 191, 13, 27)


    def draw_branch(self, startX, startY, length, variation_X, variation_Y, thickness):
        for position in range(length):
            self.display.rectangle(startX - (position - (length * variation_X)), (startY - (length * variation_Y)) - position, thickness, thickness)
            self.display.rectangle(startX + (position + (length * variation_X)), (startY - (length * variation_Y)) - position, thickness, thickness)
            self.display.rectangle(startX + (position - (length * variation_X)), (startY - (length * variation_Y)) - position, thickness, thickness)
            self.display.rectangle(startX - (position + (length * variation_X)), (startY - (length * variation_Y)) - position, thickness, thickness)

        
    def draw_branches(self):
        startX = 118 ## starting X position based on trunk
        startY = 180 ## starting Y position based on trunk
        length = 10 ## initial branchlength
        variation_X = [0, 1, 2, 2, 3, 2, 1, 1, 2, 1, 1, 1, 0, 0]
        variation_Y = [0, 1, 1, 2, 3, 3, 3, 3, 4, 3, 4, 2, 4, 5]
        thickness = [3, 3, 2, 3, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2]
        branches = len(variation_X)
        
        for branch in range(branches):
            self.draw_branch(startX, startY, length, variation_X[branch], variation_Y[branch], thickness[branch])
            
    def generate_leaves(self, season):
        if season != "winter":
            for new_leaf in range(200):
                leaf.add_leaf(self.leaves, season, random.randrange(85, 155), random.randrange(115, 180))
            
    def draw_leaves(self):
        for leaf in self.leaves:
            self.display.set_pen(leaf.colour[0], leaf.colour[1], leaf.colour[2])
            self.display.circle(int(leaf.x), int(leaf.y), int(leaf.r))
        

    def draw_tree(self, season):
        self.display.set_pen(self.trunk_colour)
        self.draw_trunk()
        self.draw_branches()
        self.generate_leaves(season)
        self.draw_leaves()
