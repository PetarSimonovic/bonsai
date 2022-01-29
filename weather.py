import rain


class Weather:
    
    def __init__(self, display, width, height):
        self.raindrops = []
        self.display = display
        self.width = width
        self.height = height
    
    def generate_conditions(self, season):
        if season == "winter":
            snowfall()
        if season == "spring":
            self.rainfall()
            
    
    def print_test(self):
        print("Weather here")
        
    def rainfall(self):
        if len(self.raindrops) < 80:
            rain.add_raindrop(self.raindrops, self.width, self.height)

        for raindrop in self.raindrops:
            rain.fall(raindrop, self.width, self.height)
            self.display.set_pen(0, 0, raindrop.colour)
            self.display.rectangle(raindrop.x , raindrop.y, raindrop.width, raindrop.length)
            

        
