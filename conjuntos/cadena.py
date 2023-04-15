

opc = 0
while opc != 1:
    cadena = input('Ingresa una cadena\n')

    print('Cadena impresa de la forma ::2 \n{}'.format(cadena[::2]))
    print('Cadena impresa de la forma ::-1 \n{}'.format(cadena[::-1]))

    print('Cadena remplazando las letras o por f \n{}'.format(cadena.replace('o','f')))

    a = int(input('Ingresa el primer rango\n'))
    b = int(input('Ingresa el segundo rango\n'))

    print('La cadena original es {}\nCadena modificada\n{}'.format(cadena,cadena[a:b]))
    opc = int(input('Ingresa 1 para salir, cualquier otro numero para repetir\n'))
