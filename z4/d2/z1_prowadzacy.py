import json

def dane_do_zapisz():
    imie = input('Podaj imie: ')
    nazwisko = input('Podaj nazwisko: ')
    rok = input('Podaj rok: ')
    email = input('Podaj email: ')
    pensja = input('Podaj pensja: ')

    dane = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok": rok,
        "pensja": pensja
    }
    return dane

def zapisz(dane):

    with open("pracownicy.json", 'w') as f:
        json.dump(dane, f)
#pokombinować z tym enumarate
def wypisz():
    for nr, pracownik in enumerate[pracownicy, start=1]:
        print(
            f'{[nr],  Pracownik{imie}, nazwikiem {nazwisko}, zrodzony{rok}, zarabia{pensja}'
        )



try:
    with open('pracownicy.json') as f:
        pracownicy = json.load(f)
except FileNotFoundError:
    pracownicy = []

a = input("Co chcesz zrobicp [d -dodaj, w- wypisz, k - koniec] \n")
while a != "k":
    if a == "d":
        dane = dane_do_zapisz()
        zapisz(dane)
        a = input("Co chcesz zrobicp [d -dodaj, w- wypisz, k - koniec] \n")
    elif a =="w":
        wypisz()
        a = input("Co chcesz zrobicp [d -dodaj, w- wypisz, k - koniec] \n")
    elif a =="k":
        break