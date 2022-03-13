from rocket import Rocket

class Fireworks:
    
    def __init__(self, display, width, height):
        self.display = display
        self.width = width
        self.height = height
        self.rockets = [
            Rocket(display, width, height),
            Rocket(display, width, height),
            Rocket(display, width, height)]
    
    def launch(self):
        for rocket in self.rockets:
            rocket.launch()
        
    


