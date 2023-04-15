
lista = ["ITT", 21, 3.14]

print(lista[1])

print(lista)

for i,aux in enumerate(lista):
    print("Elemento {} = {}".format(i, aux))

# <id>.append(<valor>)
#     .insert(<index>, <value>)
#     .pop elimina 
# modificar <id>[<pos>] = <value>

a = lista.remove(21)

print(a)

print(lista)
