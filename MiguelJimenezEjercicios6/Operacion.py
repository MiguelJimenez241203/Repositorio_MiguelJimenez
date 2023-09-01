import Numeroelementos as NM

def main():
    try:
        n = int(input("Ingrese el valor de n "))
        m = int(input("Ingrese el valor de m "))
        
        if n < 0 or m < 0 or m > n:
            print("No es posible hacer la operación")
        else:
            resultado = NM.numero_muestras(n, m)
            print(f"El número de combinaciones posibles con los npumeros ({n}, {m}) es {resultado}")
    except ValueError:
        print("Ingreso mal algún dato")

if __name__ == "__main__":
    main()