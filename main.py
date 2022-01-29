import utime
import math
import snow
import time
from sky import Sky
from weather import Weather
from tree import Tree
from breakout_colourlcd240x240 import BreakoutColourLCD240x240


width = BreakoutColourLCD240x240.WIDTH
height = BreakoutColourLCD240x240.HEIGHT


display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display = BreakoutColourLCD240x240(display_buffer)

display.set_backlight(1.0)

sky = Sky(display, width, height)
weather = Weather(display, width, height)
tree = Tree(display, width, height)


season = "summer"



def draw_hill(season):
    if season == "spring": 
        display.set_pen(126, 200, 80)
    elif season == "summer" or season == "autumn":
         display.set_pen(126, 200, 100)
    elif season == "winter":
         display.set_pen(235, 235, 235)

    display.circle(128, 360, 185) ## x, y, radius

    

while True:
    datetime = utime.localtime() ## 0: year, 1: day, 2: month, 3: hour
    display.clear()
    sky.paint_the_sky(1)
    draw_hill(season)
    tree.draw_tree(season)
    weather.generate_conditions(season)
    display.update()
    time.sleep(0.001)
    
