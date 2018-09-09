class Product:

    def __init__(self, id, name, price, discount):
        self._id = id
        self._name = name
        self.price = price
        self._discount = discount

    @property
    def full_name(self):
        return 'Product: ' + self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value

    @property
    def discount(self):
        """maly help"""
        return self._discount

    @discount.setter
    def discount(self, dis):
        if type(dis) == float:
            if 0 <= dis <= 30:
                self._discount = dis
            elif dis < 0:
                self._discount = 0.00
            else:
                self._discount = 30.00

    #help(Pr1.discount_price)
Pr1 = Product(1, "bula", 10, 0.00)
#print(Pr1._id)
#print(Pr1._name)
#print(Pr1.price)
#print(Pr1.discount_price)
print(Pr1.name)
Pr1.name = "jajajajaja"
print(Pr1.name)
Pr1.name = "ja"
print(Pr1.name)
Pr1.discount = 0.00
print(Pr1.discount)
Pr1.discount = 50.00
print(Pr1.discount)
Pr1.discount = -5.00
print(Pr1.discount)
Pr1.discount = 27.00
print(Pr1.discount)

def test():
    Pr1.discount = 0.00
    assert Pr1.discount == 0
    Pr1.discount = 27.00
    assert Pr1.discount == 27
    Pr1.discount = 50.00
    assert Pr1.discount == 30
