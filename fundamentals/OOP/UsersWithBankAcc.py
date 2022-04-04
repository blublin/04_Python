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
        # print(f"Balance: ${self.balance:,}")
        # return self
        return self.balance
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
        self.accounts = {} # dictionary holding account names (keys) and amounts (values)

    def make_account(self, accName, intRate, balance = 0):
        self.accounts[accName] = BankAccount(intRate, balance)
    def make_deposit(self, accName, amount):
        self.accounts[accName].deposit(amount)
        return self
    def make_withdrawal(self, accName, amount):
        self.accounts[accName].withdraw(amount)
        return self
    def list_accounts(self):
        for acc in self.accounts:
            print(f"Account: {acc}")
    def display_user_balance(self, accName=''):
        if accName:
            print(f"User: {self.name}, {accName} Balance: ${self.accounts[accName].display_account_info():,}")
        else:
            for accName in self.accounts:
                print(f"User: {self.name}, {accName} Balance: ${self.accounts[accName].display_account_info():,}") 
        # self.accounts[accName].display_account_info()
        return self
    def transfer_money(self, accName, other_user, other_user_acc, amount):
        if self.accounts[accName].balance >= amount:
            self.accounts[accName].withdraw(amount)
            other_user.accounts[other_user_acc].deposit(amount)
            print(f"Successfully transfered ${amount} from {self.name}'s {accName} account to {other_user.name}'s {other_user_acc} account.")
            self.accounts[accName].display_account_info()
            other_user.accounts[other_user_acc].display_account_info()
        else:
            print("Insufficient funds.")
        return self

ben = User("Ben Lublin", "lublin.ben@gmail.com")
scsa = User("Stone Cold Steve Austin", "questions@steveaustinshow.com")
hank = User("Hank Hill", "hill@stricklandpropane.com")

ben.make_account("Savings", 3, 50829)
scsa.make_account("Checking", 5, 2309233)
hank.make_account("Propane", 2, 2000)

ben.make_deposit("Savings", 500).make_deposit("Savings", 378).make_deposit("Savings", 823).make_withdrawal("Savings", 400).display_user_balance()

scsa.make_deposit("Checking", 39474762).make_deposit("Checking", 47595733).make_withdrawal("Checking", 23436742).make_withdrawal("Checking", 12422382).display_user_balance()

hank.make_deposit("Propane", 500).make_withdrawal("Propane", 50).make_withdrawal("Propane", 50).make_withdrawal("Propane", 125).display_user_balance()

ben.transfer_money("Savings", hank, "Propane", 250)
