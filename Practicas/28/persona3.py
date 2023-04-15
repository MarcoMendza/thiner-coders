class Persona:
    # Atributos
    def __init__(self):
        self.__nombre = ""
        self.__apPat = ""
        self.__apMat = ""
        self.__edad = 0
        self.__sexo = ""
        self.__peso = 0
        self.__estatura = 0

    # Getter/Setter
    ##Nombre
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    ##Apellido Paterno
    def get_apPat(self):
        return self.__apPat

    def set_apPat(self, apPat):
        self.__apPat = apPat

    ##Apellido Materno
    def get_apMat(self):
        return self.__apMat

    def set_apMat(self, apMat):
        self.__apMat = apMat

    ##Edad
    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    ##Sexo
    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = sexo

    ##Peso
    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    ##Estatura
    def get_estatura(self):
        return self.__estatura

    def set_estatura(self, estatura):
        self.__estatura = estatura

    # Metodos
    def nombreCompleto(self):
        print("El nombre es: ", self.__nombre, "", self.__apPat, "", self.__apMat)

    def getIMC(self):
        print(self.__peso / (self.__estatura * self.__estatura))

    def imprimirDatos(self):
        self.nombreCompleto()
        self.getIMC()


##Main
def main():
    persona1 = Persona()
    persona1.set_nombre("Jose")
    persona1.set_apPat("Trejo")
    persona1.set_apMat("Moreno")
    persona1.set_edad(22)
    persona1.set_sexo("H")
    persona1.set_peso(78)
    persona1.set_estatura(1.82)
    persona1.getIMC()
    persona1.nombreCompleto()
    persona1.imprimirDatos()


if __name__ == '__main__':
    main()
