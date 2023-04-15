'''
 Nombre de la persona 
 Edad
 Imprimir que sea mayor de edad 
'''

nombre = input("Ingresa tu nombre\n")
edad = int(input("Ingresa tu edad\n"))

if edad >= 18:
    print("{} es mayor de edad".format(nombre))
else:
    print("{} es menor de edad".format(nombre))
