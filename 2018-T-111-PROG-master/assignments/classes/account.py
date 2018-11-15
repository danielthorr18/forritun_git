class Account:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return "Balance: {:.2f}".format(self.balance)


class SavingsAccount(Account):
    INTEREST_RATE = 0.05
    BONUS_RATE = 0.10

    def update_balance(self):
        self.balance = self.balance * (1 + self.INTEREST_RATE) + (self.balance * self.BONUS_RATE) 


class DebitAccount(Account):
    INTEREST_RATE = 0.02

    def update_balance(self):
        self.balance = self.balance * (1 + self.INTEREST_RATE)


def print_accounts(accounts):
    for account in accounts:
        print(account)

def update_accounts(accounts):
    for account in accounts:
        account.update_balance()

s1 = SavingsAccount(300)
s1.update_balance()
print(s1)
