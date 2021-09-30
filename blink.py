## test file to check that pico is connected properly: will make it's LED turn on/off

from machine import Pin
led = Pin(25, Pin.OUT)

led.toggle()