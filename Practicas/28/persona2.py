class Persona():
    __nombre = ""
    __apPaterno = ""
    __apMaterno = ""
    __edad = 0
    __sexo = ""
    __peso = 0
    __estatura = 0


    def llenado(self):
        self.__nombre = input('Ingresa nombre ')
        self.__apPaterno = input('Ingresa Apellido Paterno ')
        self.__apMaterno = input('Ingresa Apellido Materno ')
        self.__edad = int(input('Ingresa tu edad '))
        self.__sexo = input('Ingresa tu sexo ')
        self.__peso = float(input('Ingresa tu peso '))
        self.__estatura = float(input('Ingresa tu estatura '))

    def nombreCompleto(self):
        return self.__nombre + ' ' + self.__apPaterno + ' ' + self.__apMaterno

    def idice(self):
        return self.__peso / self.__estatura**2

    def imprimir(self):
        print('Nombre: {} \nApellido Paterno {} \nApellido Materno: {}\nEdad: {}'
              '\nSexo: {}\nPeso: {}\nEstatura: {}'.format(self.__nombre, self.__apMaterno,
                                                          self.__apPaterno, self.__edad, self.__sexo,
                                                          self.__peso, self.__estatura))


if __name__ == "__main__":
    p1 = Persona()
    print('Nombre completo : {}'.format(p1.nombreCompleto()))
    print('Indice de masa corporal {}'.format(p1.idice()))
    p1.imprimir()
