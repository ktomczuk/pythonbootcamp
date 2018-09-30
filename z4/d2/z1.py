import json
#coursera - darmowy kurs pythona
lista = []
a = 0
#with open("example.json") as f:
#    lista = json.load(f)

def zapisz():
    id = 1
    lista.append(id)
    ob = input('Podaj imie: ')
    lista.append(ob)
    ob = input('Podaj nazwisko: ')
    lista.append(ob)
    ob = input('Podaj rok: ')
    lista.append(ob)
    ob = input('Podaj email: ')
    lista.append(ob)
    id += 1


def wypisz():
    with open("lista.json", 'w') as f:
        json.dump(lista, f)
    print(lista)


while a != "k":
    a = input("Co chcesz zrobicp [d -dodaj, w- wypisz, k - koniec] \n")
    if a == "d":
       zapisz()
    elif a =="w":
        wypisz()
    elif a =="k":
        break