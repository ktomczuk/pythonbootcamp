
def formatuj(*napisy, **znacznik):
    napisy = "\n".join(napisy)
    napisy = napisy.replace(napisy)
    for znacznik in napisy:
        print(znacznik)
    return


def test_formatuj_napis_bez_znacznikow():
    assert formatuj('Hello world') == "Hello world"

def test_formatuj_napisy_bez_znacznikow():
    assert formatuj('Hello world', 'Im Rafal') == "Hello world\nIm Rafal"

def test_formatuj_napisy_znacznik():
    assert formatuj('Hello world', 'Im Rafal', cena=10) == "Hello world\nIm Rafal\ncena=10"