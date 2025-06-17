class Vehicle:
    def start(self):
        print("vehicle startedd...")
    
class car(Vehicle):
    def start(self):
        print("car is starting with a key....")


class bike(Vehicle):
    def start(self):
        print("bike is starting with a kick....")


V = Vehicle()
c = car()
b = bike()

V.start()
c.start()
b.start()
