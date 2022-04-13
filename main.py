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
from chatterbot import Chatterbot

width = BreakoutColourLCD240x240.WIDTH
height = BreakoutColourLCD240x240.HEIGHT


display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display = BreakoutColourLCD240x240(display_buffer)

display.set_backlight(1.0)

season = "autumn"
precipitation = "rain"
day = True

sky = Sky(display, width, height)
moon = Moon(display, width, height)
weather = Weather(display, width, height)
hill = Hill(display, width, height)
tree = Tree(display, width, height, season)
fireworks = Fireworks(display, width, height)
chatterbot = Chatterbot(display)

def update_scene():
    display.update()
    time.sleep(0.001)
    display.clear

while True:
    
    print(gc.mem_free()) # prints memory
    datetime = utime.localtime() ## 0: year, 1: day, 2: month, 3: hour
    sky.paint_the_sky(2, day)
    moon.rise()
    # fireworks.launch()
    hill.draw_grass(season)
    tree.draw_tree()
    weather.generate_conditions(precipitation)
   # chatterbot.tell_the_time()
    chatterbot.babble(datetime)
    update_scene()
    gc.collect()
    
