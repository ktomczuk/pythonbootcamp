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

a_label = tkinter.Label(master=root, text="a")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="b")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

wynik_label = tkinter.Label(master=root, text="")
wynik_label.pack()


dodaj_button = tkinter.Button(master=root, text="Dodaj", command=zlacz_napisy )
dodaj_button.pack()

czysc_button = tkinter.Button(master=root, text="Czysc", command=czysc_napisy )
czysc_button.pack()


root.mainloop()
