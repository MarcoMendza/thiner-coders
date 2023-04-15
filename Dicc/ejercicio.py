
opc = 0 
while opc != 1:
    n = int(input("Ingrese el número de elementos de la lista: "))
    lista = []
    for i in range(n):
        elemento = input(f"Ingrese el elemento {i+1}: ")
        lista.append(elemento)
    lista_sin_repetidos = list(set(lista))
    diccionario = {}
    for i in range(len(lista_sin_repetidos)):
        diccionario[i+1] = lista_sin_repetidos[i]
    print("Lista sin repetidos: ", lista_sin_repetidos)
    print("Diccionario: ", diccionario)
    opc = int(input('Ingresa 1 para salir, cualquier otro numero para continuar '))
