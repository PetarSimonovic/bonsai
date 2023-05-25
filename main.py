import utime
import time
import gc


from breakout_colourlcd240x240 import BreakoutColourLCD240x240

from sky import Sky
from weather import Weather
from tree import Tree
from hill import Hill
from fireworks import Fireworks
from moon import Moon
from timebot import Timebot

width = BreakoutColourLCD240x240.WIDTH
height = BreakoutColourLCD240x240.HEIGHT


display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display = BreakoutColourLCD240x240(display_buffer)

display.set_backlight(0.3)

season = "summer"
precipitation = "none"
day = False
celebration = True

sky = Sky(display, width, height)
moon = Moon(display, width, height)
weather = Weather(display, width, height)
hill = Hill(display, width, height)
tree = Tree(display, width, height, season)
fireworks = Fireworks(display, width, height)
timebot = Timebot(display)

def update_scene():
    display.update()
    time.sleep(0.03)
    display.clear

while True:
    
    # print(gc.mem_free()) # prints memory
    datetime = utime.localtime() ## 0: year, 1: day, 2: month, 3: hour
    hour = datetime[3]
    sky.paint_the_sky(8, day)
    if not day:
        moon.rise()
        if celebration:
            fireworks.launch()
    hill.draw_grass(season)
    tree.draw_tree()
    weather.generate_conditions(precipitation)
    timebot.tell_the_time(datetime)
    update_scene()
    gc.collect()
    

