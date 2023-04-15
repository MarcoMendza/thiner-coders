
lim = int(input("Ingresa los terminos a imprimir\n"))
aux = 3
print(lim)
for i in range(lim):
    print(aux)
    if i%2 == 0:
        aux += 2
    else:
        aux += 3
    
