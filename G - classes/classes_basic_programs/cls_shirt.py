"""
   write a python programme on shirts.
"""

class shirt():
    def __init__(self, colour, price, company):
        self.colour = colour
        self.price = price
        self.company = company

    def get_details(self):
        return self.price, self.colour, self.company

    def set_name(self, company):
        self.company = company


c = shirt("blue", "500", "polo")
print(c.get_details())
#c.set_name("lenin")
print(c.get_details())


class Pant(shirt):
    def __init__(self, colour, price, company, size):
        self.size = size
        super().__init__(colour, price, company)
         #    or  #
        #shirt.__init__(self,colour, price, company)
    pass


p = Pant("red", 600, "coolkhakies", 38)
print(p.get_details())


