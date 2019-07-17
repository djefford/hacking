class BankAccount:
  def __init__(self):
    self.balance = 0
  
  def withdraw(self, amount):
    self.balance -= amount
    return print(self.balance)

  def deposit(self, amount):
    self.balance += amount
    return print(self.balance)


a = BankAccount()
b = BankAccount()

a.deposit(100)
b.deposit(50)

a.withdraw(10)
b.withdraw(10)