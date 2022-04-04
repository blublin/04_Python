from webbrowser import BackgroundBrowser


class BankAccount:
    all_accounts = []
    def __init__(self, intRate, balance = 0):
        self.intRate = intRate * 0.01
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.intRate
        return self
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

account01 = BankAccount(2)
account02 = BankAccount(3)

account01.deposit(534).deposit(234).deposit(634).withdraw(500).yield_interest().display_account_info()

account02.deposit(237).deposit(8347).withdraw(2874).withdraw(4234).withdraw(342).withdraw(5000).yield_interest().display_account_info()

BankAccount.all_balances()