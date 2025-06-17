class Student:
    school = "abc"  # same for everyone
    def __init__(self, name):
        self.name= name

s1= Student("shr")
s2= Student("akas")
print(s1.name)
print(s2.name)