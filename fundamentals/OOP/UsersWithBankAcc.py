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
        print(f"Balance: ${self.balance:,}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.intRate
        return self
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(3,100)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self
    def transfer_money(self, other_user, amount):
        if self.account.balance >= amount:
            self.account.withdraw(amount)
            other_user.account.deposit(amount)
            print(f"Successfully transfered ${amount} from {self.name} to {other_user.name}.")
            self.account.display_account_info()
            other_user.account.display_account_info()
        else:
            print("Insufficient funds.")
        return self

ben = User("Ben Lublin", "lublin.ben@gmail.com")
scsa = User("Stone Cold Steve Austin", "questions@steveaustinshow.com")
hank = User("Hank Hill", "hill@stricklandpropane.com")

ben.make_deposit(500).make_deposit(378).make_deposit(823).make_withdrawal(400).display_user_balance()

scsa.make_deposit(39474762).make_deposit(47595733).make_withdrawal(23436742).make_withdrawal(12422382).display_user_balance()

hank.make_deposit(500).make_withdrawal(50).make_withdrawal(50).make_withdrawal(125).display_user_balance()

ben.transfer_money(hank, 250)
