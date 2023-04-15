
'''
Si ingresa un numero postivo 
Negativo 
Cero
'''

num = int(input("Ingresa un numero\n"))

if num > 0:
    print("El numero {} es mayor a cero".format(num))
elif num < 0: 
    print("El numero {} es menor a cero".format(num))
else:
    print("El numero {} es igual a cero".format(num))
