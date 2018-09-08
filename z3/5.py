class Product:
    def __init__(self, id, name, price):
        self.id = 1
        self.name = 'Woda'
        self.price = 10.99

    def print_info(self):
        return f'"{self.name}", id: {self.id}, cena: {self.price} PLN'




class Basket():
    def __init__(self):
        self.entries = 0

class Basket_entry():
    def __init__(self, Product, ilosc):
        self.Product = Product
        self.ilosc = ilosc
        if Product in self.entries:
            pass
        




def test_basket_ini():
    basket = Basket()
    assert basket.entries == 0

def test_add_product():
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product,5)
    assert len(basket, ilosc)
def test_add_product_twice
    ():
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)

    assert basket.count_total_price()
    assert basket.generate_report()
