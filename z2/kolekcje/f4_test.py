def dodawanie(a, b):
    #if type(a) == str:
    #    a = 0
    #if type(b) == str:
    #    b = 0
    wynik = a + b
    return wynik

def mnozenie(a, b):
    #if type(a) == str:
    #    a = 0
    #if type(b) == str:
     #   b = 0
    wynik = a * b
    return wynik


def test_dodawanie():
    assert dodawanie(1, 1) == 2
    assert dodawanie('y', 'y') == 'yy'
    assert mnozenie(1, 1) == 1
    assert mnozenie(1, 0) == 0
   # assert mnozenie('a', 'a') == 'aa'