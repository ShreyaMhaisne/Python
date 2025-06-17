class claculor:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
       return self.a+self.b

    def sub(self):
      return self.a-self.b
    
    def multiply(self):
      return self.a * self.b
    
    def divide(self):
       return self.a / self.b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

cal = claculor(num1 , num2)

print("addition ",cal.add())
print("subtraction ",cal.sub())
print("divide ",cal.divide())
print("multiplication ",cal.multiply())

        