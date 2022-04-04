class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        # "User: Guido van Rossum, Balance: $150
    def transfer_money(self, other_user, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            other_user.make_deposit(amount)
            print(f"Successfully transfered ${amount} from {self.name} to {other_user.name}.")
            self.display_user_balance()
            other_user.display_user_balance()
        else:
            print("Insufficient funds.")

ben = User("Ben Lublin", "lublin.ben@gmail.com")
scsa = User("Stone Cold Steve Austin", "questions@steveaustinshow.com")
hank = User("Hank Hill", "hill@stricklandpropane.com")

ben.make_deposit(500)
ben.make_deposit(378)
ben.make_deposit(823)
ben.make_withdrawal(400)
ben.display_user_balance()

scsa.make_deposit(39474762)
scsa.make_deposit(47595733)
scsa.make_withdrawal(23436742)
scsa.make_withdrawal(12422382)
scsa.display_user_balance()

hank.make_deposit(500)
hank.make_withdrawal(50)
hank.make_withdrawal(50)
hank.make_withdrawal(125)
hank.display_user_balance()

ben.transfer_money(hank, 250)
