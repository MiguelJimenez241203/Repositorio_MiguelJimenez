def clasificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "isósceles"
    else:
        return "escaleno"

def es_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1

try:
    lado1 = float(input("Ingrese la longitud del primer lado: "))
    lado2 = float(input("Ingrese la longitud del segundo lado: "))
    lado3 = float(input("Ingrese la longitud del tercer lado: "))
    
    if es_triangulo(lado1, lado2, lado3):
        tipo_triangulo = clasificar_triangulo(lado1, lado2, lado3)
        print(f"Se puede formar un triángulo {tipo_triangulo}.")
    else:
        print("No se puede formar un triángulo con esas longitudes.")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos para las longitudes de los lados.")
