from breakout_colourlcd240x240 import BreakoutColourLCD240x240
import math
import time

width = BreakoutColourLCD240x240.WIDTH
height = BreakoutColourLCD240x240.HEIGHT

display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display = BreakoutColourLCD240x240(display_buffer)

display.set_backlight(1.0)

    
def check_colour(colour):
    if colour > 255:
        return 255
    else:
        return colour
    
def get_RGB(time, layer):
    red = check_colour(int((math.cos(math.radians(time)) * 255) * 0.5) + layer ) 
    green = check_colour(int((math.sin(math.radians(time)) * 58) * 2) + layer)
    blue = check_colour(int((math.tan(math.radians(time)) * 23) * 3) + layer)
    display.set_pen(red, green, blue)

def paint_the_sky(time):
    layer = 0
    for sky_layer in range(11):
        get_RGB(int(time * 7.5), layer)
        display.rectangle(0, layer, width, int(height/12))
        layer += int(height/12)
    display.update()

def sunrise():
    for hour in range(12):
        paint_the_sky(hour)
        time.sleep(1)
        
sunrise()