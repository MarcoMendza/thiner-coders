
class Persona:
    def nombreCompleto(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
    
    def getIMC(self, peso):
        estatura_metros = self.estatura / 100
        return peso / (estatura_metros ** 2)
    
    def imprimirDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido Paterno: {self.apellido_paterno}")
        print(f"Apellido Materno: {self.apellido_materno}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Estatura: {self.estatura} cm")

    def getattribute(self, nombre_attr):
        if nombre_attr == 'nombre':
            return self._nombre
        elif nombre_attr == 'apellido_paterno':
            return self._apellido_paterno
        elif nombre_attr == 'apellido_materno':
            return self._apellido_materno
        elif nombre_attr == 'edad':
            return self._edad
        elif nombre_attr == 'sexo':
            return self._sexo
        elif nombre_attr == 'estatura':
            return self._estatura
        else:
            return super().getattribute(nombre_attr)

    def setattr(self, nombre_attr, valor):
        if nombre_attr == 'nombre':
            self._nombre = valor
        elif nombre_attr == 'apellido_paterno':
            self._apellido_paterno = valor
        elif nombre_attr == 'apellido_materno':
            self._apellido_materno = valor
        elif nombre_attr == 'edad':
            self._edad = valor
        elif nombre_attr == 'sexo':
            self._sexo = valor
        elif nombre_attr == 'estatura':
            self._estatura = valor
        elif nombre_attr == 'peso':
            self._peso = valor
        else:
            super().setattr(nombre_attr, valor)

    def nombre(self):
        return self._nombre
    
    def nombre(self, valor):
        self._nombre = valor
        
    def apellido_paterno(self):
        return self._apellido_paterno
    
    def apellido_paterno(self, valor):
        self._apellido_paterno = valor
        
    def apellido_materno(self):
        return self._apellido_materno
    
    def apellido_materno(self, valor):
        self._apellido_materno = valor
        
    def edad(self):
        return self._edad
    
    def edad(self, valor):
        self._edad = valor
        
    def sexo(self):
        return self._sexo
    
    def sexo(self, valor):
        self._sexo = valor
        
    def estatura(self):
        return self._estatura
    
    def estatura(self, valor):
        self._estatura = valor

if __name__ == "__main__":
    p1 = Persona()

    p1.setattr('nombre', 'Gabriel')
    p1.setattr('apellido_paterno', 'Villafania')
    p1.setattr('apellido_materno', 'Gomez')
    p1.setattr('sexo', 'Hombre')
    p1.setattr('edad', 23)
    p1.setattr('peso', 75)
    p1.setattr('estatura_metros', '1.72')
    p1.getIMC()
    p1.nombreCompleto()
    p1.imprimirDatos()
