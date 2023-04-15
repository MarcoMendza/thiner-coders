
def serie(a, b):
    num1 = a
    aux = a
    i = 0
    aux2 = num1
    while i <= b:
        aux = 3
        while aux >= 1:
            print(aux2, end = ' ')
            aux2 -= 1
            aux -= 1
            i += 1
        num1 += 1
        aux2 = num1

if __name__ == "__main__":
    a = int(input('Ingresa el valor del primer numero de la serie\n -> '))
    b = int(input('Ingresa cuantos terminos va a imprimir\n -> '))
    serie(a, b)
