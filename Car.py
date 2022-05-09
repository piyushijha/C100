class Car: 
    def __init__(self, speed, colour, win): 
        self.speed = speed
        self.colour = colour
        self.win = win

    def message(self):
        print("The race has been postponed")

car1 = Car(20, "red", 100)
car1.message()
