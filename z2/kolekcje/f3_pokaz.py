def policz_znaki(napis):
    poziom = 0
    il_poziomow = 0
    for i in napis:
        if i == '<':
            poziom += 1
            continue
        elif i == '>':
            poziom -= 1
            continue
        il_poziomow += poziom
    return il_poziomow



def test_zero_znakow():
    assert policz_znaki('') == 0

def test_zero_znakow_w():
    assert policz_znaki('Alaaaaaaa<>aaaa ma kota') == 0

def test_2_znaki():
    assert policz_znaki('Alaaaaaaa<bb>aaaa ma kota') == 2

def test_3_znaki():
    assert policz_znaki('Alaaaaaaa<<bcb>>aaaa ma kota') == 6