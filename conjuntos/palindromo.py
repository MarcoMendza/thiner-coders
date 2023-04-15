
opc = 0
while opc != 1:
    cadena = input('Ingresa una cadena para comprobar si es palindroma\n')
    aux = cadena.replace(' ','')[::-1].lower()
    aux1 = cadena.replace(' ','').lower()
    if aux==aux1:
        print('La cadena es palindroma')
    else:
        print('No es palindroma')
    opc = int(input('Ingresa 1 para salir, cualquier otro numero para repetir\n-> '))
