# In this assignment you will help a new bank get up and running. 
# The Bank is called Happy Bank and it has two kinds of accounts, a savings account and a debit account. 
# You will need to use inheritance in this assignment so you will need to figure out what the 
#  account types have in common and what they don´t. 
# The accounts should have a method called update_balance() which updates the balance.
# A savings account updates the balance as follows:
# It updates the balance by its interest rate and adds a bonus rate to it. 
# For a savings account the interest rate is 5% and the bonus rate is 10%.
# A debet account updates the balance as follows:
# It updates the balance by its interest rate which is 2 % for debet accounts.
# HINT: think about using class variables for the constants (interest rate and bonus rate).
# You also need to implement the __str__() method. Think about where you should implement it. 
# You only need to implement it once. Look at the output example here below to figure out what 
#  string the method should return.
# You also need to implement the functions print_accounts() which should print each account and 
#  update_accounts() which should call the method update_balance() on each account.
# def main():
#     s1 = SavingsAccount(1000)
#     d1 = DebitAccount(1000)
#     s2 = SavingsAccount(2000)
#     d2 = DebitAccount(4000)
#     accounts = [s1, d1, s2, d2]
#     print_accounts(accounts)
#     update_accounts(accounts)
#     print_accounts(accounts)
#     update_accounts(accounts)
#     print_accounts(accounts)
#     update_accounts(accounts)
# Output:
# Balance: 1000.00
# Balance: 1000.00
# Balance: 2000.00
# Balance: 4000.00
# Balance: 1150.00
# Balance: 1020.00
# Balance: 2300.00
# Balance: 4080.00
# Balance: 1322.50
# Balance: 1040.40
# Balance: 2645.00
# Balance: 4161.60

# You should only hand in the code for the class
class Accounts():
    BONUS_RATE = 0
    INTEREST_RATE = 0
    def __init__(self, balance=0.0):
        self.balance = balance

    def __str__(self):
        return "Balance: {:.2f}".format(self.balance)
    
    def update_balance(self):
        self.balance += self.balance*self.INTEREST_RATE + self.balance*self.BONUS_RATE
        return self.balance


class SavingsAccount(Accounts):
    BONUS_RATE = 0.10
    INTEREST_RATE = 0.05


class DebitAccount(Accounts):
    BONUS_RATE = 0
    INTEREST_RATE = 1.02




def main():
    s1 = SavingsAccount(1000)
    d1 = DebitAccount(1000)
    s2 = SavingsAccount(2000)
    d2 = DebitAccount(4000)
    accounts = [s1, d1, s2, d2]
    print_accounts(accounts)
    update_accounts(accounts)
    print_accounts(accounts)
    update_accounts(accounts)
    print_accounts(accounts)
    update_accounts(accounts)