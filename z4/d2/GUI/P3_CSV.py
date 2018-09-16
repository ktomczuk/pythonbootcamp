import csv
with open("dane.csv") as f:
    dane_pliku = csv.DictReader(f)
    suma = 0
    for row in dane_pliku:
        #suma += row['Revenue']
        print(row['Product'])
            #print(column)#['lp'])
    #print(suma)