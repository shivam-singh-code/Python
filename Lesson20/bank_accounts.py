class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName) -> None:
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\n Balance = ${self.balance:.2f}")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' has balance = {self.balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has balance of ${self.balance:.2f}")
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\n Withdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withdraw interrupted: {error}")
    
    def transfer(self, amount, account):
        try:
            print('\n************\n\nBeginning Transfer.. 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\n Transfer complete! ✔\n\n**********')
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")

class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete!")
        self.getBalance()

class SavingsAcct(InterestRewardAcct):
    def __init__(self, initialAmount, acctName) -> None:
        super().__init__(initialAmount, acctName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance  = self.balance - (amount + self.fee)
            print("\nWithdraw Completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted! {error}")