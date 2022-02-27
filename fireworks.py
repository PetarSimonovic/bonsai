import random
import sparks 

class Fireworks:
    
    def __init__(self, display, width, height):
        self.display = display
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.sparks = []
        
    def launch(self):
        print("launching fireworks")
        self.get_centre()
        if (len(self.sparks) == 0):
            self.create_sparks()
        else:
            self.fly_sparks()
        
    def create_coordinate(self, range):
        return random.randint(0, range)
    
    
    def get_centre(self):
        self.x = self.create_coordinate(self.width)
        self.y = self.create_coordinate(round(self.height/2))
        print(self.x, self.y)
    
    def create_sparks(self):
        print("adding sparks!")
        while (len(self.sparks) < 50):
            for spark in range(50):
                sparks.add_sparks(self.sparks, spark, self.x, self.y)
       
    def fly_sparks(self):
        print("sparks fly")
        for spark in self.sparks:
            self.display.set_pen(spark.colour[0], spark.colour[1], spark.colour[2])
            self.display.circle(int(spark.dx), int(spark.dy), int(spark.r))
