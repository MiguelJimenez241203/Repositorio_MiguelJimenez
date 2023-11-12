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
    

def mostrar(ciudadano):
    print(f'-------Clase 2023-II -----\n')
    for i in ciudadano:
        print(f'\n\
        Nombre: {i.getNombre()}\n\
        Cédula: {i.getCedula()}\n\
        Edad: {i.getEdad()}\n')
        if i.getEdad() <18:
            print('--Es menor de edad')
        else:
            print('--Es mayor de edad--')

class Carrera(Ciudadano):
    def __init__(self):
        super().__init__()

def main():
    ciudadano=[]
    while True:
        print('''
            (1) Ejecutar el programa
            (2) Salir
            ''')
        opc=int(input('¿Qué opción va a escoger (1/2): '))
        if opc == 1:
            while 1:
                est=Ciudadano()
                est.setNombre(input('Ingrese su nombre completo: '))
                est.setEdad(int(input('Ingrese su edad: ')))
                est.setCedula(input('Ingrese su número de cédula: '))
                ciudadano.append(est)
                mostrar(ciudadano)
                opc2=input('¿Desea agregar mas gente? (Y/N): ')
                if opc2 == 'N':
                    break
                else:
                    print('Regresando al programa')

        if opc == 2:
            print('Saliendo de todo el programa...')
            break
        
if __name__=="__main__":
    main()