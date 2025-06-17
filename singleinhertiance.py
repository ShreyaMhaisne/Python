class Animal:
    def sound(self):
        print("animal makes a sound ")

class dog(Animal):
    def bark(self):
        print("dog barks ")

d = dog()
d.sound()
d.bark()
