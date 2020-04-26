class Car:
    # Properties
    color = ""
    brand = ""
    number_of_wheels = 4
    number_of_seates = 4
    maxspeed = 0

    # constructor
    def __init__(self, color, brand, number_of_wheels, number_of_seates, maxspeed):
        self.color = color
        self.brand = brand
        self.number_of_seates = number_of_seates
        self.number_of_wheels = number_of_wheels
        self.maxspeed = maxspeed

    # Create method set color
    def setcolor(self, x):
        self.color = x

    # Create method set brand

    def setbrand(self, x):
        self.brand = x

     # Create method set brand

    def setspeed(self, x):
        self.maxspeed = x

    def printdata(self):
        print("Color of thsi car is : ", self.color)
        print("Brand of thsi car is : ", self.brand)
        print("Maxspeed of thsi car is : ", self.maxspeed)

    # Deconstructor

    def __del__(self):
        print()
