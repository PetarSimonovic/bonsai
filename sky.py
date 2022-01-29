import random
import utime
import math
import snow
import rain
import leaf
import time
from sky import Sky
from breakout_colourlcd240x240 import BreakoutColourLCD240x240


sky = Sky()
width = BreakoutColourLCD240x240.WIDTH
height = BreakoutColourLCD240x240.HEIGHT


display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display = BreakoutColourLCD240x240(display_buffer)

display.set_backlight(1.0)

snowflakes = []
raindrops = []
leaves = []
season = "spring"

if season != "winter":
    for new_leaf in range(200):
        leaf.add_leaf(leaves, season, random.randrange(85, 155), random.randrange(115, 180))

trunk = display.create_pen(118, 82, 46)


def draw_hill(season):
    if season == "spring": 
        display.set_pen(126, 200, 80)
    elif season == "summer" or season == "autumn":
         display.set_pen(126, 200, 100)
    elif season == "winter":
         display.set_pen(235, 235, 235)

    display.circle(128, 360, 185) ## x, y, radius

def draw_trunk():
    display.rectangle(115, 180, 10, 30) ## x, y, width, height
    display.rectangle(113, 200, 13, 15)
    display.rectangle(115, 191, 13, 27)


def draw_branch(startX, startY, length, variation_X, variation_Y, thickness):
    for position in range(length):
        display.rectangle(startX - (position - (length * variation_X)), (startY - (length * variation_Y)) - position, thickness, thickness)
        display.rectangle(startX + (position + (length * variation_X)), (startY - (length * variation_Y)) - position, thickness, thickness)
        display.rectangle(startX + (position - (length * variation_X)), (startY - (length * variation_Y)) - position, thickness, thickness)
        display.rectangle(startX - (position + (length * variation_X)), (startY - (length * variation_Y)) - position, thickness, thickness)

    
def draw_branches():
    startX = 118 ## starting X position based on trunk
    startY = 180 ## starting Y position based on trunk
    length = 10 ## initial branchlength
    variation_X = [0, 1, 2, 2, 3, 2, 1, 1, 2, 1, 1, 1, 0, 0]
    variation_Y = [0, 1, 1, 2, 3, 3, 3, 3, 4, 3, 4, 2, 4, 5]
    thickness = [3, 3, 2, 3, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    branches = len(variation_X)
    
    for branch in range(branches):
        draw_branch(startX, startY, length, variation_X[branch], variation_Y[branch], thickness[branch])
        
def draw_leaves():
    for leaf in leaves:
        display.set_pen(leaf.colour[0], leaf.colour[1], leaf.colour[2])
        display.circle(int(leaf.x), int(leaf.y), int(leaf.r))
    

def draw_tree():
    display.set_pen(trunk)
    draw_trunk()
    draw_branches()
    draw_leaves()

def weather(season):
    if season == "winter":
        snowfall()
    if season == "spring":
        rainfall()
        
    
    
def snowfall():
    if len(snowflakes) < 80:
        snow.add_snowflake(snowflakes, width, height)

    for snowflake in snowflakes:
        snow.fall(snowflake, width, height)
        display.set_pen(snowflake.colour, snowflake.colour, snowflake.colour)
        display.circle(int(snowflake.x), int(snowflake.y), int(snowflake.r))

def rainfall():
    if len(raindrops) < 80:
        rain.add_raindrop(raindrops, width, height)

    for raindrop in raindrops:
        rain.fall(raindrop, width, height)
        display.set_pen(0, 0, raindrop.colour)
        display.rectangle(raindrop.x , raindrop.y, raindrop.width, raindrop.length)
        

    
while True:
    datetime = utime.localtime() ## 0: year, 1: day, 2: month, 3: hour
    display.clear()
    sky.paint_the_sky(5, display, width, height)
    draw_hill(season)
    draw_tree()
    weather(season)
    display.update()
    time.sleep(0.001)
    
