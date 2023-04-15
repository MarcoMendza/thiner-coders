
'''
Hacer la serie 
Impresa 

Serie de pi
'''

def divisiones(n):
    i = 0
    aux = 1
    flag = True
    while i < n:
        if flag:
            if i == n-1:
                print('4/{}'.format(aux), end = ' ')
            else:
                print('4/{} - '.format(aux), end = ' ')
            aux += 2
            flag = False
        else:
            if i == n-1:
                print('4/{}'.format(aux), end = ' ')
            else:
                print('4/{} + '.format(aux), end = ' ')
            aux += 2 
            flag = True
        i += 1



if __name__ == "__main__":
    i = int(input('Ingresa el numero de iteraciones\n-> '))
    divisiones(i)
