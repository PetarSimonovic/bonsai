import random
import spark 

class Fireworks:
    
    def __init__(self, display, width, height):
        self.display = display
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.sparks = []
        
    def create_coordinate(self, range):
        return random.randint(0, range)
    
    
    def get_centre(self):
        self.x = self.create_coordinate(self.width)
        self.y = self.create_coordinate(round(self.height/2))
        print(self.x, self.y)
        
    def launch(self):
        print("launching fireworks")
        self.get_centre()
        spark.add_sparks(self.sparks, self.x, self.y)
        
        
        
        
    
