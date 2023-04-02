##Implement a program for encapsulation

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount()
account.deposit(1000)
account.withdraw(500)
print("Balance:", account.get_balance())
