def policz_znaki(tekst):
    p1 = tekst.rfind("<")
    k1 = tekst.rfind(">")
    z1 = k1 - p1 - 1
    print(f'liczba znakow powmiedzy to: {z1}')
    return z1


def test_zero_znakow():
    assert policz_znaki('Alaaaaaaa<>aaaa ma kota') == 0
def test_3_znakow():
    assert policz_znaki('Alaaaaaaa<qwe>aaaa ma kota') == 3