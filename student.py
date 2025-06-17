class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks=marks
# is used to access instance variable
    def display(self):
        if(self.marks>70):
            print("pass with distinction ")
        elif (self.marks > 60):
            print("pass")
        elif (self.marks >40):
            print("Atkt")
        else:
            print("fail")

name = str(input("enter name"))
num1 = int(input("enter a no"))

stu = Student(name,num1)

stu.display()