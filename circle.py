class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        are=2*3.14*self.radius
        print("area of circle is :",are)


c = Circle(3)
c.area()
