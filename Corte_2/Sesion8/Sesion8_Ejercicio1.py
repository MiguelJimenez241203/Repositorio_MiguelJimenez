def main(filas, columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num=int(input(f'Ingrese el número de la posición [{i},{j}]: '))
            matriz[i].append(num)
    
    for i in matriz:
        print(i)
    #return matriz

if __name__=="__main__":
    filas=int(input('Ingrese el numero de filas: '))
    columnas=int(input('Ingrese el numero de columnas: '))
    main(filas,columnas)