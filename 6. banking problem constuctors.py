class Account:
    def __init__(self,balance,account):
        self.balance = balance
        self.account = account

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs: {amount} is deducted fom your account now your balance is {self.getbalance()}")

    def credit(self,amount):
        self.balance += amount
        print(f"Rs: {amount} is added to your account now your balance is {self.getbalance()}")
    def getbalance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.credit(1000)
acc1.debit(9000)