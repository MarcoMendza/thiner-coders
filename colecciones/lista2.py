# Imprimir la lista, ordenar, Imprimir, reverse, Imprimir

inicio = True
lista = []
while inicio:
    ele = input('Ingrese el elemento\n-> ')
    if ele == '0':
        inicio = False
    else:
        lista.append(ele)

print("Lista: \n{}".format(lista))
lista.sort()
print("Lista ordenada: \n{}".format(lista))
lista.reverse()
print("Lista invertida: \n{}".format(lista))

