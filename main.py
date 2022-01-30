import utime
import math
import snow
import time
from sky import Sky
from weather import Weather
from tree import Tree
from hill import Hill
import gc
from breakout_colourlcd240x240 import BreakoutColourLCD240x240

width = BreakoutColourLCD240x240.WIDTH
height = BreakoutColourLCD240x240.HEIGHT


display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display = BreakoutColourLCD240x240(display_buffer)

display.set_backlight(1.0)

season = "spring"


sky = Sky(display, width, height)
weather = Weather(display, width, height)
hill = Hill(display, width, height)
tree = Tree(display, width, height, season)

    

while True:
    print(gc.mem_free())
    datetime = utime.localtime() ## 0: year, 1: day, 2: month, 3: hour
    display.clear()
    sky.paint_the_sky(2)
    hill.draw_hill(season)
    tree.draw_tree()
    weather.generate_conditions(season)
    display.update()
    time.sleep(0.001)
    gc.collect()
    
