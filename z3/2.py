class Product:
    def __init__(self, id, name, price):
        self.id = 1
        self.name = 'Woda'
        self.price = 10.99

    def print_info(self):
        return f'"{self.name}", id: {self.id}, cena: {self.price} PLN'

def test_produkt():
    product = Product(1, 'Woda', 10.99)
    assert product.id == 1
    assert product.name == 'Woda'
    assert product.price == 10.99

def test_pritn_produkt():
    product = Product(1, 'Woda', 10.99)
    assert product.print_info() == '"Woda", id: 1, cena: 10.99 PLN'

# jak dodamy capsys
#def test_pritn_produkt2(capsys):
#    product = Product(1, 'Woda', 10.99)
#    product.print_info()
#    wyjscie = capsys.readouterr()
#    out = wyjscie[0]
#    assert out == '"Woda", id: 1, cena: 10.99 PLN\n'
#    product = Product(1, 'Piwo', 10.99)
#    out, _ = capsys.readouterr()
#    assert out == '"Woda", id: 1, cena: 10.99 PLN\n'