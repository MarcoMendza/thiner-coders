class Alumno:
    def __init__(self, nombre, apPat, apMat, edad, noCtrl, semestre, nomMaterias):
        self.__nombre = nombre
        self.__apPat = apPat
        self.__apMat = apMat
        self.__edad = edad
        self.__noCtrl = noCtrl
        self.__semestre = semestre
        self.__nomMaterias = nomMaterias
        # self.__calificaciones = calificaciones

    def __getNomCompleto(self):
        return self.__nombre + " " + self.__apPat + " " + self.__apMat

    def imprimirDatos(self):
        print("Nombre: {}\nApellido Paterno: {}\nApeliido Materno: {}\nEdad: {}\nNumero de Control: {}\n"
              "Semestre: {}\nNombre de Materias: {}".format(self.__nombre, self.__apPat, self.__apMat,
                                                            self.__edad, self.__noCtrl, self.__semestre,
                                                            self.__nomMaterias))  # self.__calificaciones)
'''

    def getCalif(self):
        return self.__calificaciones

    def getPromedio(self):
        return sum(self.__calificaciones.values()) / len(self.__calificaciones)
'''

def llenadoMaterias():
    materias = []
    while True:
        dato = input('Ingresa los nombres de materias (o "hecho" para finalizar): ')
        if dato == "hecho":
            break
        materias.append(dato)
    return materias


if __name__ == "__main__":
    op = 0
    while op != 1:
        alumnos = []
        num = int(input('Cuantos alumnos desea registrar? '))
        while num > 0:
            nombre = input('Ingresa el nombre ')
            apPat = input('Ingresa apellido paterno ')
            apMat = input('Ingresa apellido materno ')
            edad = int(input('Ingresa la edad '))
            noCtrl = input('Ingresa numero de control ')
            semestre = int(input('Ingresa el semestre '))
            nomMaterias = llenadoMaterias()
            alumno = Alumno(nombre, apPat, apMat, edad, noCtrl, semestre, nomMaterias)
            alumnos.append(alumno)
            num -= 1
        for alumno in alumnos:
            alumno.imprimirDatos()
        op = int(input('Ingresa 1 para salir, cualquier otro numero para repetir'))

