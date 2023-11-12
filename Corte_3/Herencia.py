class Ciudadano:
    def __init__(self):
        self.__nombre=None
        self.__edad=None
        self.__cedula=None

    def setNombre(self, nombre:str):
        self.__nombre=nombre
        
    def getNombre(self):
        return self.__nombre

    def setEdad(self, edad:int):
        if edad< 0:
            print('Edad no válida')
        else: 
            self.__edad=edad

    def getEdad(self):
        return self.__edad

    def setCedula(self,cedula:int):
        if len(cedula) >=8 and len(cedula) <=10:
            self.__cedula=cedula
        else:
            print('--El número de cédula es inválido--')
        
    def getCedula(self):
        return self.__cedula
    
    def mostrarInfo(self):
        print(f'\n\
        Nombre: {self.getNombre()}\n\
        Cédula: {self.getCedula()}\n\
        Edad: {self.getEdad()}\n')

class Estudiante(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__carrera = None
        self.__semestre = None

    def setCarrera(self, carrera: str):
        self.__carrera = carrera

    def getCarrera(self):
        return self.__carrera

    def setSemestre(self, semestre: int):
        self.__semestre = semestre

    def getSemestre(self):
        return self.__semestre

    def mostrarInfo(self):
        print(f'\n\
        Nombre: {self.getNombre()}\n\
        Cédula: {self.getCedula()}\n\
        Edad: {self.getEdad()}\n\
        Carrera: {self.getCarrera()}\n\
        Semestre: {self.getSemestre()}\n')

class Doctor(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__especialidad = None
        self.__experiencia = None

    def setEspecialidad(self, especialidad: str):
        self.__especialidad = especialidad

    def getEspecialidad(self):
        return self.__especialidad

    def setExperiencia(self, experiencia: int):
        self.__experiencia = experiencia

    def getExperiencia(self):
        return self.__experiencia

    def mostrarInfo(self):
        print(f'\n\
        Nombre: {self.getNombre()}\n\
        Cédula: {self.getCedula()}\n\
        Edad: {self.getEdad()}\n\
        Especialidad: {self.getEspecialidad()}\n\
        Experiencia: {self.getExperiencia()} años\n')

class Ingeniero(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__especialidad = None
        self.__proyectos_realizados = None

    def setEspecialidad(self, especialidad: str):
        self.__especialidad = especialidad

    def getEspecialidad(self):
        return self.__especialidad

    def setProyectosRealizados(self, proyectos: int):
        self.__proyectos_realizados = proyectos

    def getProyectosRealizados(self):
        return self.__proyectos_realizados

    def mostrarInfo(self):
        print(f'\n\
        Nombre: {self.getNombre()}\n\
        Cédula: {self.getCedula()}\n\
        Edad: {self.getEdad()}\n\
        Especialidad: {self.getEspecialidad()}\n\
        Proyectos Realizados: {self.getProyectosRealizados()}\n')

def main():
    ciudadano = []
    while True:
        print('''
            (1) Agregar Ciudadano
            (2) Agregar Estudiante
            (3) Agregar Doctor
            (4) Agregar Ingeniero
            (5) Mostrar Información
            (6) Salir
            ''')
        opc = int(input('¿Qué opción va a escoger (1-6): '))
        if opc == 1:
            ciu = Ciudadano()
            ciu.setNombre(input('Ingrese su nombre completo: '))
            ciu.setEdad(int(input('Ingrese su edad: ')))
            ciu.setCedula(input('Ingrese su número de cédula: '))
            ciudadano.append(ciu)
        elif opc == 2:
            est = Estudiante()
            est.setNombre(input('Ingrese su nombre completo: '))
            est.setEdad(int(input('Ingrese su edad: ')))
            est.setCedula(input('Ingrese su número de cédula: '))
            est.setCarrera(input('Ingrese su carrera: '))
            est.setSemestre(int(input('Ingrese su semestre: ')))
            ciudadano.append(est)
        elif opc == 3:
            doc = Doctor()
            doc.setNombre(input('Ingrese su nombre completo: '))
            doc.setEdad(int(input('Ingrese su edad: ')))
            doc.setCedula(input('Ingrese su número de cédula: '))
            doc.setEspecialidad(input('Ingrese su especialidad médica: '))
            doc.setExperiencia(int(input('Ingrese años de experiencia: ')))
            ciudadano.append(doc)
        elif opc == 4:
            ing = Ingeniero()
            ing.setNombre(input('Ingrese su nombre completo: '))
            ing.setEdad(int(input('Ingrese su edad: ')))
            ing.setCedula(input('Ingrese su número de cédula: '))
            ing.setEspecialidad(input('Ingrese su especialidad ingenieril: '))
            ing.setProyectosRealizados(int(input('Ingrese cantidad de proyectos realizados: ')))
            ciudadano.append(ing)
        elif opc == 5:
            for c in ciudadano:
                c.mostrarInfo()
        elif opc == 6:
            print('Saliendo de el programa...')
            break

if __name__ == "__main__":
    main()
