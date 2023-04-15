
def getCalculo(a, b):
    return a+b, a-b, a*b, a//b, a**b

if __name__ == "__main__":
    a= int(input('Ingresa el valor para a\n->'))
    b = int(input('Ingresa el valor de b \n->'))
    x, y, z, c, d = getCalculo(a, b)
    print("La suma es: {}".format(x))
    print("La resta es: {}".format(y))
    print("La multiplicación es: {}".format(z))
    print("La división es: {}".format(c))
    print("La potencia es: {}".format(d))
