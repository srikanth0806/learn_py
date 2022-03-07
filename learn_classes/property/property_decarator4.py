"      PROPETY CONCEPT IN CLASSES    ,  MODEL-2  ,  EXAMPLE-2    "
class Car:

    def __init__(self,name,company,price):
        self.name=name
        self.company=company
        self.price=price

    @property
    def method(self):
        return self.company

    @method.setter
    def method(self,company):
         self.company = company

    @method.deleter
    def method(self,company):
        self.company


s=Car("fortuner","toyota",2000000)
print(s.method)
s.company="suzuki"
print(s.method)
