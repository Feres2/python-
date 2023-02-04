class BankAccount:
    all_accounts=[]
    def __int__(self,int_rate=0.2,balance=0):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self
    def withdraw(self,amount):
        if (self.balance>=amount):
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a 5dollar fee")
            self.balance -= 5
        return self