my_dict = dict()
my_dict['python'] = "Lanzua"
my_dict['html'] = "hyper"

my_dict = {
    'python': 'jezyczek',
    'ruby': 'kotlin',
    'c++': 'wow'
}
print(my_dict)
my_s_dict = dict([('a', 'pierwsza'), ('b', 'druga')])
print(dir(my_dict))
print(my_dict.keys())
print(my_dict.items())
print(my_dict.values())
lista_jezykow = ['python', 'c++', 'c#', 'assembler']
for lang in lista_jezykow:
    print(my_dict.get(lang, "Nie znam tego jeszcze"))

print(len(my_dict))
print(dir(my_dict))