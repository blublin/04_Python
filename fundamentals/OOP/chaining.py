class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            other_user.make_deposit(amount)
            print(f"Successfully transfered ${amount} from {self.name} to {other_user.name}.")
            self.display_user_balance()
            other_user.display_user_balance()
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
