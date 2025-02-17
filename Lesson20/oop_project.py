from bank_accounts import *

Dave = BankAccount(1000,"Dave")
Jack = BankAccount(2000,"Jack")

Dave.getBalance()

Jack.deposit(500)

# Dave.withdraw(2000)
Dave.transfer(500, Jack)

Jim = InterestRewardAcct(1000, "JIM")

Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(10000, Jim)
Blaze.transfer(200, Jim)