
opc = 2
flag = True
while opc != 1:
    num = int(input("Ingresa un numero para saber si es primo\n"))

    
    for i in range(2, 9):
        if num!=i:
            if num%i ==0:
                flag = True
    if flag:
        print("No es primo")
    else:
        print("Es primo")
    opc = int(input("Si desea salir ingresa 1"))
