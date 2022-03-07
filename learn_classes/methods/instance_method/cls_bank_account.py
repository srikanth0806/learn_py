#creation of bank acount.
class Bank_Account:
    def __init__(self,bankname,account_holder_name,account_number,
                 password, ammount=0):
        self.bank_name = bankname
        self.account_holder_name=account_holder_name
        self.account_number=account_number
        self.ammount = ammount
        self.password=password

    def deposit(self, money):
        if money > 0:
            self.ammount += money
            print("deposit completed")

    def with_draw(self, money):
        psw = input("Please enter password:")
        if psw == self.password:
            if self.ammount >= money:
                self.ammount = self.ammount - money
            else:
                print("sufficient funds not available")
        else:
            print("invalid password given")

    def check_balance(self):
        print("available balance is %d" %self.ammount)


x=Bank_Account("SBI","SRIKANTH","0678 9876 562","TSTK2019")

x.check_balance()

x.deposit(500)
x.check_balance()
x.with_draw(200)
x.check_balance()
x.with_draw(500)
