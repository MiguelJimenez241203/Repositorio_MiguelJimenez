import Funcion_externa
import Ejemplos

def main():
    nombre = input('Ingrese su nombre ')
    surname = input('Ingrese su apellido ')
    print('--------------')
    Funcion_externa.matrix(nombre,surname)
    print('--------------')
    print(f'Ejecutado desde {__name__}')
    print('+++++++++++++')
    a=int(input('Ingrese un número '))
    b=int(input('Ingrese un número '))
    Ejemplos.suma(a,b)
    print('+++++++++++++')


    #Funcion_externa.operacio()
    #s()
if __name__=="__main__":
    main()

