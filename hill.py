
class Hill:
    
    def __init__(self, display, width, height):
        self.display = display
        self.width = width
        self.height = height
    
    
    
    def draw_hill(self, season):
         if season == "spring": 
            self.display.set_pen(126, 200, 80)
         elif season == "summer" or season == "autumn":
            self.display.set_pen(126, 200, 100)
         elif season == "winter":
            self.display.set_pen(235, 235, 235)

         self.display.circle(128, 300, 210) ## x, y, radius

