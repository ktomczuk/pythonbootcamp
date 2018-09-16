#tutaj grid zamiast pack i ustawiamy elementy

import tkinter
def zlacz_napisy():
    a = a_entry.get()
    b = b_entry.get()
    #print(a+b)  -> wedy w konsoli
    wynik_label.configure(text=f"Wynik: {a+b}")

def czysc_napisy():
    a = a_entry.get()
    b = b_entry.get()
    #print(a+b)  -> wedy w konsoli
    wynik_label.configure(text=f"")

root = tkinter.Tk()
root.title("Prosty kalkulator")
#root.columnconfigure(1, weight=1)


a_label = tkinter.Label(master=root, text="a")
a_label.grid(row=0, column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0, column=1)

b_label = tkinter.Label(master=root, text="b")
b_label.grid(row=1, column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1, column=1)

wynik_label = tkinter.Label(master=root, text="")
wynik_label.grid(row=2, column=0)


dodaj_button = tkinter.Button(master=root, text="Dodaj", command=zlacz_napisy )
dodaj_button.grid(row=3, column=0)

czysc_button = tkinter.Button(master=root, text="Czysc", command=czysc_napisy )
czysc_button.grid(row=3, column=1)


root.mainloop()
