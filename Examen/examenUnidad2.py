class MatrizIdentidad:
    def __init__(self, fila, col):
        self.fila = fila
        self.col = col
        self.lista = [[0 for x in range(fila)] for y in range(col)]

    def llenarMatriz(self, escalar=1):
        for i in range(self.fila):
            for j in range(self.col):
                if i == j:
                    self.lista[i][j] = escalar
                else:
                    self.lista[i][j] = 0

    def imprimirMatriz(self):
        for i in range(self.fila):
            for j in range(self.col):
                print(self.lista[i][j], end=" ")
            print()

    def cambiarDato(self, fila, columna, dato):
        self.lista[fila][columna] = dato


if __name__ == "__main__":
    fila = int(input("Ingrese el numero de filas: "))
    col = int(input("Ingrese el numero de columnas: "))
    MI = MatrizIdentidad(fila, col)
    while True:
        print("\nMENU")
        print("a) Llenar matriz o cambiar escalar")
        print("b) Imprimir matriz")
        print("c) Cambiar un dato de una fila y columna")
        print("s) Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "a":
            escalar = int(input("Ingrese el escalar: "))
            MI.llenarMatriz(escalar)
        elif opcion == "b":
            MI.imprimirMatriz()
        elif opcion == "c":
            fila = int(input("Ingrese la fila: "))
            columna = int(input("Ingrese la columna: "))
            dato = int(input("Ingrese el nuevo dato: "))
            MI.cambiarDato(fila, columna, dato)
        elif opcion == "s":
            break
        else:
            print("Opcion no valida")
