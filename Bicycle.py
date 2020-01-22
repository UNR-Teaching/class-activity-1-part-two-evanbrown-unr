from Wheel import *
from Vehicle import *

class Bicycle(Vehicle):

    wheels = Wheel("bicycle")

    def __init__(self, style, color, year):
        Vehicle.__init__(self, color, year)
        self.style = style
    
    def show_info(self):
        print(self.style + " bike, year " + self.year + "( " + self.color + " )")
        self.wheels.show_info()
        
    def pedal(self):
        print("Pedaling bicycle")
