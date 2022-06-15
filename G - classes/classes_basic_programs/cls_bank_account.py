"""
creation of bank account.
"""


class BankAccount:
    def __init__(self, bank_name, account_holder_name, account_number,
                 password, amount=0):
        self.bank_name = bank_name
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.amount = amount
        self.password = password

    def deposit(self, money):
        if money > 0:
            self.amount += money
            print("deposit completed")

    def with_draw(self, money):
        psw = input("Please enter password:")
        if psw == self.password:
            if self.amount >= money:
                self.amount = self.amount - money
            else:
                print("sufficient funds not available")
        else:
            print("invalid password given")

    def check_balance(self):
        print("available balance is %d" % self.amount)


x = BankAccount("SBI", "SRIKANTH", "0678 9876 562", "TSTK2019")

x.check_balance()

x.deposit(500)
x.check_balance()
x.with_draw(200)
x.check_balance()
x.with_draw(500)
