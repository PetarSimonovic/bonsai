import rain
import snow

class Weather:

    def __init__(self, display, width, height):
        self.raindrops = []
        self.snowflakes = []
        self.display = display
        self.width = width
        self.height = height
        print("Weather here")
        print(self.display)

    def generate_conditions(self, season):
        if season == "winter":
            self.snowfall()
        if season == "spring":
            self.rainfall()


    def rainfall(self):
        if len(self.raindrops) < 80:
            rain.add_raindrop(self.raindrops, self.width, self.height)

        for raindrop in self.raindrops:
            rain.fall(raindrop, self.width, self.height)
            self.display.set_pen(0, 0, raindrop.colour)
            self.display.rectangle(raindrop.x , raindrop.y, raindrop.width, raindrop.length)



    def snowfall(self):
        if len(self.snowflakes) < 80:
            snow.add_snowflake(self.snowflakes, self.width, self.height)

        for snowflake in self.snowflakes:
            snow.fall(snowflake, self.width, self.height)
            self.display.set_pen(snowflake.colour, snowflake.colour, snowflake.colour)
            self.display.circle(int(snowflake.x), int(snowflake.y), int(snowflake.r))
