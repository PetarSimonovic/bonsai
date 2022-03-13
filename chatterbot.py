class Chatterbot:
    
    def __init__(self, display):
        self.display = display
        # x and y define top left corner of text
        self.x = 10
        self.y = 220
        # wrap is number of pixels before text wraps
        self.wrap = 250
           
    def babble(self, datetime):
        self.display.set_pen(22, 22, 29)
        if self.decide_what_to_say() == "time":
            text = self.format_date_time(datetime)
        self.display.text(text, self.x, self.y, self.wrap)
    
    def decide_what_to_say(self):
        return "time"
    
    def format_date_time(self, datetime):
        months = {
            1 : "January",
            2 : "February",
            3 : "March",
            4 : "April",
            5 : "May",
            6 : "June",
            7 : "July",
            8 : "August",
            9 : "September",
            10 : "October",
            11 : "November",
            12 : "December",}

        return str(datetime[2]) + " " + months[datetime[1]] + " " + str(datetime[0])