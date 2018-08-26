
def wiecej_niz(tekst, ile):
    ##tekst = str(input('Podaj tekst: '))
    licznik = {}
    wynik = set()
    for litera in tekst:
        if tekst.count(litera) > ile:
            wynik.add(litera)
    return wynik
 #   if tekst == '':
  #      print('zero znakow')
   #     return False
   # else:
   #     for i in tekst:
   #         licznik[i] = licznik.get(i, 0) + 1

    #    for i in licznik:
    #        if licznik[i] >= ile:
    #            print(f' Litera {i} wystapila: {licznik[i]}')
    #            return licznik
    #        else:
    #            return False


def test1():
    assert wiecej_niz('Alaaaaaaaaaaa ma kota', 1)
    assert wiecej_niz('Alaaaaaaaaaaa ma kota', 1) == {'a'}


def test2():
    assert wiecej_niz('', 2)


def test3():
    assert wiecej_niz('Joooooooooooooooooooooooo', 5)


def test4():
    assert wiecej_niz('Joooooooooooooooooooooooo', 5) == set()
#def jakas(tekst)
