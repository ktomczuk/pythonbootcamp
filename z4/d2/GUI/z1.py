import tkinter
def oblicz_cene():
    a = float(dystans_entry.get())
    b = float(spalanie_entry.get())
    c = float(paliwo_entry.get())

    wynik_label.configure(text=f"Koszt przejazdu: {a*b*c/100} PLN")

def czysc_wynik():
    wynik_label.configure(text=f"")

root = tkinter.Tk()
root.title("Prosty kalkulator")
#root.columnconfigure(1, weight=1)


dystans_label = tkinter.Label(master=root, text="Podaj dystans")
dystans_label.grid(row=0, column=0)
dystans_entry = tkinter.Entry(master=root)
dystans_entry.grid(row=0, column=1)

spalanie_label = tkinter.Label(master=root, text="Podaj spalanie")
spalanie_label.grid(row=1, column=0)
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.grid(row=1, column=1)

paliwo_label = tkinter.Label(master=root, text="Podaj cewne paliwa")
paliwo_label.grid(row=2, column=0)
paliwo_entry = tkinter.Entry(master=root)
paliwo_entry.grid(row=2, column=1)


wynik_label = tkinter.Label(master=root, text="")
wynik_label.grid(row=3, column=0)


oblicz_button = tkinter.Button(master=root, text="oblicz", command=oblicz_cene )
oblicz_button.grid(row=4, column=0)

czysc_button = tkinter.Button(master=root, text="Czysc", command=czysc_wynik )
czysc_button.grid(row=5, column=0)


root.mainloop()
