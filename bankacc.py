class bankAccount:
    def __init__(self, name ,bankbalance):
        self.name = name
        self.bankbalance= bankbalance
    
    def deposit(self, amount):
        self.bankbalance += amount
        print("deposit succeffullly",self.bankbalance)

    def withdraw(self, amount):
        if amount > self.bankbalance:
            print("insufficient balance ")
        else:
            self.bankbalance -= amount
            print("withdraw ",self.bankbalance)

name = input("enter your name ")
initial_balance = float(input("Enter initial balance: "))

acc = bankAccount(name, initial_balance)

dep = float(input("enter amount to deposit :"))
acc.deposit(dep)

wd = float(input("enter anoumt to withdraw"))
acc.withdraw(wd)

        