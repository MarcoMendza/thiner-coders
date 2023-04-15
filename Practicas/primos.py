
'''
Un metodo que diga si es numero primo
'''

def numPrimo(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input('Ingresa un numero\n-> '))
    if numPrimo(n):
        print('Es un numero primo')
    else:
        print('No es primo')
