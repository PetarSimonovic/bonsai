
class Moon:
    
    
    def __init__(self, display, width, height):
        self.display = display
        self.width = width
        self.height = height
        self.radius = 20
        
    def rise(self):
        x = self.width/2
        y = 50
        self.draw_luna(x, y)
#         self.draw_shadow(x, y)
    
    def draw_luna(self, x, y):
        self.draw_circle(180, x, y, self.radius)
        self.draw_circle(220, x - 5, y, self.radius)
        self.draw_circle(210, x - 10, y - 10, self.radius/3.5)
        self.draw_circle(210, x - 7, y + 8, self.radius/4)
        self.draw_circle(210, x - 9, y + 5, self.radius/3)
        self.draw_circle(200, x + 5, y - 6, self.radius/5)
        self.draw_circle(200, x + 8, y + 3, self.radius/4)
        
    def draw_shadow(self, x, y):
        self.draw_circle(0, x + 15, y, self.radius)

    
    def draw_circle(self, hue, x, y, r):
        self.display.set_pen(hue, hue, hue)
        self.display.circle(int(x), int(y), int(r))
    
 
