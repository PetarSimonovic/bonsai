
class Moon:
    
    
    def __init__(self, display, width, height):
        self.display = display
        self.width = width
        self.height = height
        self.radius = 20
        
    def rise(self):
        x = self.width/2
        y = 50
        self.display.set_pen(180, 180, 180)
        self.display.circle(int(x), int(y), int(self.radius))
        self.display.set_pen(220, 220, 220)
        self.display.circle(int(x - 5), int(y), int(self.radius))
        self.display.set_pen(210, 210, 210)
        self.display.circle(int(x - 10), int(y - 10), int(self.radius/3.5))
        self.display.set_pen(210, 210, 210)
        self.display.circle(int(x - 7), int(y + 8), int(self.radius/4))
        self.display.circle(int(x - 9), int(y + 5), int(self.radius/3))
        self.display.set_pen(208, 208, 208)
        self.display.circle(int(x + 5), int(y - 6), int(self.radius/5))
        self.display.circle(int(x + 8), int(y + 3), int(self.radius/4))
