
class Moon:
    
    
    def __init__(self, display, width, height):
        self.display = display
        self.width = width
        self.height = height
        
    def rise(self):
        self.display.set_pen(200, 200, 200)
        self.display.circle(int(self.width/2), int(50), int(20))
