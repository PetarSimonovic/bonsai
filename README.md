# terrarium
Digital terrarium  for Raspberry Pi Pico, witten in MicroPython

A digital terrarium written in MicroPython for a [Raspberry Pi Pico](https://shop.pimoroni.com/products/raspberry-pi-pico?variant=32402092294227) mounted with a [BreakoutColourLCD240x240](https://shop.pimoroni.com/products/1-3-spi-colour-lcd-240x240-breakout?variant=30250963632211&currency=GBP&utm_source=google&utm_medium=cpc&utm_campaign=google+shopping?utm_source=google&utm_medium=surfaces&utm_campaign=shopping&gclid=Cj0KCQjwwNWKBhDAARIsAJ8HkhfexBZbHZXHZKI0WixTnGqXf9Q40DyJy6te9mpHibEGymhLaVfnP_4aAhWKEALw_wcB). 

The code, written using the [Thonny](https://thonny.org) and based on [Pimorini's st7789](https://github.com/pimoroni/st7789-python) library, creates a simple nature scene. It will change in real-time, simulating the seasons alongside weather conditions, sunrises and sunsets.    


**Existing features**

(currently need to be manually implemented, ie they're not yet tied to the clock)

- snowfall
- basic sunrise, sunset and sky tones
- leaves, with seasonal colours

**In development**
- rainfall
- leafall
- leaf growth
- greater variation in branch shapes
- cloud cover
- greater variety in sky colours
- tie everything to the clock: ultimately the terrarium should use the date/time to generate a seasonal scene

