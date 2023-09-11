def divisores_numero():
    numero = int(input("Ingrese un número: "))
    
    if numero == 0:
        print("Ningún número es divisible entre cero")
    else:
        print(f"Los divisores de {numero} son:")
        for i in range(1, numero + 1):
            if numero % i == 0:
                print(i)

def producto_enteros():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
    producto = 0
    for _ in range(abs(num2)):
        producto += abs(num1)
    
    if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
        producto = -producto
    
    print(f"El producto de {num1} y {num2} es: {producto}")

def serie_fibonacci():
    cantidad_digitos = int(input("Ingrese la cantidad de dígitos de la serie Fibonacci a mostrar: "))
    
    a, b = 0, 1
    print("Serie de Fibonacci:")
    for _ in range(cantidad_digitos):
        print(a, end=", ")
        a, b = b, a + b
    print()