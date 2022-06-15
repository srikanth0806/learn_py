class Cars:
    def __init__(self, name, colour, price, company):
        self.name = name      #private mode
        self.colour = colour   #protected mode
        self.price = price       #public mode
        self.company = company

    def get_vals(self):
        print(self.name, self.colour, self.price, self.company)

    def set_name(self, name):
        self.name = name


x=Cars("fortuner", "red", " 25 l", "toyota")
# calling 3 types through object, which are shown below:
x.get_vals()
Cars.get_vals(x)
type(x).get_vals(x)


"""NOTE:
        values 'updation' and 'getting' the values are recomonded by methods"""

x.set_name("maruthi")

x.get_vals()
