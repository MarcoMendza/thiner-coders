
rep = 1 
while rep == 1:
    suma = 1
    print("Bienvenido al factorial")
    fact = int(input("Ingresa un numero para ser factorial\n"))
    if fact == 0:
        print("El factorial de 0 es 1")
    elif fact > 0:
        while fact != 0:
            suma *= fact    
            fact -=1
        print("El factorial es: {}".format(suma))
    else:
        print("Opcion invalida")
    rep = int(input("Si desea repetir el programa ingrese 1, si desea salir ingrese otro numero\n"))

