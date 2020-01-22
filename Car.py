
from Wheel import *
from Vehicle import *

class Car(Vehicle):

    wheels = Wheel("car")
    
    def __init__(self, make, model, color, year):
        Vehicle.__init__(self, color, year)
        self.make = make
        self.model = model
        
    def show_info(self):
        print(self.make + " " + self.model + ", year " + self.year + "( " + self.color + " )")
        self.wheels.show_info()
        
    def start(self):
        print("Starting car")

        

