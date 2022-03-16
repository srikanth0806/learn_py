"      PROPETY CONCEPT IN CLASSES    ,  MODEL-1  ,  EXAMPLE-2    "
class Car:

    def __init__(self,name,company,price):
        self.name=name
        self.company=company
        self.price=price

    def get_company(self):
        return self.company

    def set_company(self,company):
         self.company = company

    def del_company(self):
        del self.company

    compa=property(get_company,set_company,del_company)
s=Car("fortuner","toyota",2000000)
print(s.compa)
s.compa="suzuki"
print(s.compa)
