#liczba = int(input('Podaj liczbe: '))
# pip install pytest
# settings -> unit -> test runner na pytesta zmienic


def czy_jest_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


#print(czy_jest_pierwsza(liczba))

def test_czy_jest_pierwsxza():
    assert czy_jest_pierwsza(7)
    assert czy_jest_pierwsza(2)

def test_czy_jest_niepierwsza():
    assert not czy_jest_pierwsza(4)
    assert not czy_jest_pierwsza(8)