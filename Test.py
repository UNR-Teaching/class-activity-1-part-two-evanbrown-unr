from Car import *
from Bicycle import *

def test():
    car = Car("Ford","Pinto", "white", "1986")
    bike = Bicycle("BMX", "black", "1990")
    car.show_info()
    bike.show_info()
    
if __name__ == "__main__":
    test()
