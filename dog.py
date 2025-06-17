class dog:
    def __init__(self , name ,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)

d = dog("brumo",3)
d.display()