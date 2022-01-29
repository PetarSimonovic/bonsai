import math

class Sky:
    
    def __init__(self, display, width, height):
        self.display = display
        self.width = width
        self.height = height
        print("Sky here")
        print(self.display)
    
    def check_colour(self, colour):
        if colour > 255:
            return 255
        else:
            return colour
    
    def get_RGB(self, time, layer, display):
        red = self.check_colour(int((math.cos(math.radians(time)) * 60) * 2) + layer ) 
        green = self.check_colour(int((math.sin(math.radians(time)) * 50) * 2) + layer)
        blue = self.check_colour(int((math.tan(math.radians(time)) * 50) * 2) + layer)
        self.display.set_pen(red, green, blue)

    def paint_the_sky(self, time):
        layer = 0
        for sky_layer in range(11):
            self.get_RGB(int(time * 7.5), layer, self.display)
            self.display.rectangle(0, layer, self.width, int(self.height/12))
            layer += int(self.height/12)

