class Timebot:
    
    def __init__(self, display):
        self.display = display
        # x and y define top left corner of text
        self.x = 20
        self.y = 220
        # wrap is number of pixels before text wraps
        self.wrap = 250
           
    def tell_the_time(self, datetime):
        self.display.set_pen(118, 82, 46)
        text = self.format_date_time(datetime)
        self.display.text(text, self.x + 5, self.y, self.wrap)
        
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
        date = str(datetime[2]) + " " + months[datetime[1]] + " " + str(datetime[0])
        time = str(datetime[3]) + "." + str(datetime[4]) + ":" + str(datetime[5])
        return date + " " + time

