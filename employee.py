class Employee:
    company = "TCS"

    def __init__(self,name,salry):
        self.name=name    #instance variable
        self.salry=salry  # instance variable
    
    def display(self):
        print("employyee ",self.name)
        print("salary ",self.salry)
        print("comapny name ",Employee.company)

Emp = Employee("shrey",200000)
Emp.display()