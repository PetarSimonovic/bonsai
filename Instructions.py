## initisalise

from breakout_colourlcd240x240 import BreakoutColourLCD240x240

width = BreakoutColourLCD240x240.WIDTH
height = BreakoutColourLCD240x240.HEIGHT

display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display = BreakoutColourLCD240x240(display_buffer)


## set backlight with value between 0 and 1

display.set_backlight(1.0)

## display.set_pen: sets the active drawing colour as an RGB value

display.set_pen(0, 0, 0)
display.clear()
display.update()

## then draw light-grey circle on display's top left corner

display.set_pen(200, 200, 200)
display.circle(14, 14, 14)
display.update()

## when animating, clear display for each frame then remember to set_pen for each element individually

## SHAPES

## solid rectangle
display.rectangle(x_pos, y_pos, x_length, y_length)

## solid circle
display.circle(x_pos, y_pos, radius)
