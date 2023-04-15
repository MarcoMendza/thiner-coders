'''
Realizar la siguiente serie
3 2 1 4 3 2 5 4 3 6 5 4 7 6 5 ...
Hasta un número de términos que indique el usuario (debe ser mayor o igual que 12). 40 pts Debe poder repetir el programa. 20 pts
'''

print('Bienvenido al programa')
opc = 1
while opc != 0:
    print()
    termino = int(input('Ingrese el numero de terminos: '))
    if termino < 12:
        print('Opcion invalida')
    else:
        num1 = 3
        aux = 3
        i = 0
        aux2 = num1
        while i <= termino:
            aux = 3
            while aux >= 1:
                print(aux2, end = ' ')
                aux2 -= 1
                aux -= 1
                i += 1
            num1 += 1
            aux2 = num1
    opc = int(input('\nSi desea repetir el programa ingrese un numero distinto al 0 \n-> '))
