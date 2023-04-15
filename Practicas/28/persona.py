
class Persona():
    def __init__(self, nombre, apPat, apMat, edad, sexo, peso, estatura):
        self.__nombre = nombre
        self.__apPat = apPat
        self.__apMat = apMat
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__estatura = estatura
    
    def nombreCompleto(self):
        return self.__nombre +' '+ self.__apPat + ' ' + self.__apMat

    def getIMC(self):
        return float(self.__peso)/(float(self.__estatura)**2)

    def imprimirDatos(self):
        print('Nombre: {} {} {}\nEdad: {}\nSexo: {}\nPeso: {}\nEstatura: {}'.format(self.__nombre, self.__apMat,
                                                                                    self.__apPat, self.__edad,
                                                                                    self.__sexo, self.__peso, self.__estatura))


if __name__ == "__main__":
    p1 = Persona('Gabriel', 'Villafania','Gomez',26,'Hombre', 75, 1.72)
    print('Nombre completo : {}'.format(p1.nombreCompleto()))
    print('Indice de masa corporal {}'.format(p1.getIMC()))
    p1.imprimirDatos()
