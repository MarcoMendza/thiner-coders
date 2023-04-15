
'''
    conjunto.add
    conjunto.expand
    conjunto.discard
    conjunto.pop.
'''
conjunto = set()

opc = 0

print(conjunto)
while opc!=1:
    opc = int(input('Seleccione 1 para salir, cualquier numero para continuar\n-> '))
    if opc != 1:
        conjunto.add(input('Ingrese un dato\n-> '))
print(conjunto)

