def encontrar_posicion(a,b,start=0,posicion=[]):
    lista1=len(a)
    lista2=len(b)
    if lista2>lista1:
        return posicion
    elif a[:lista2]==b:
        posicion.append(start)
        encontrar_posicion(a[1:],b,start+1,posicion)
        return posicion
    else:
        encontrar_posicion(a[1:],b,start+1,posicion)
        return posicion



def main():
    a=input("Digite la primera palabra/frase: ")
    b=input("Digite la segunda palabra/frase: ")
    print(encontrar_posicion(a,b))
    


if __name__=="__main__":
    main()