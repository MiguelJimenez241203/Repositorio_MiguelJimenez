import random as r

def main():
    pass 

def mayor_elemento(lista):
    if len(lista) == 1:
        return lista[0]
    comparacion=mayor_elemento(lista[1:])
    if lista[0] > comparacion:
        return lista[0]
    else:
        return comparacion



if __name__=="__main__":
    fila=int(input('Ingrese el numero de filas: '))
    
    lista=r.sample(range(1,20),fila)
    print(lista)

    numeromayor=mayor_elemento(lista)
    print(f'El numero mayor de la lista es',numeromayor)

    main()