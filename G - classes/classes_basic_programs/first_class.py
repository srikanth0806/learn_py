"""module documentation"""


class Bag:
    def __init__(self, names, prices, materials):
        self.name = names
        self.price = prices           # instance variables
        self.material = materials

    def set_name(self, name):
        self.name = name

    def set_price(self, price):    # these are instance methods
        self.price = price

    def set_material(self, mat):
        self.material = mat

    def read_vals(self):
        print(self.name, self.price, self.material)


b1 = Bag("sky_bag", 500, "cotton")
b1.read_vals()
b1.set_name("vip")
b1.read_vals()
b1.set_price(1000)
b1.read_vals()
b1.name = "Hand_looms"
print(b1.name)
