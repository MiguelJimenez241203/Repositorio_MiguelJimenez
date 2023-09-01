def main(filas,columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num= int(input(f'ingrese el número de la posición [{i},{j}]:'))
            matriz[i].append(num)
    return matriz

if __name__=="__main__":
    filas=int(input('Ingrese el número de filas: '))
    columnas=(int(input('Ingrese el numero de columnas: ')))
    print(main(filas,columnas))
