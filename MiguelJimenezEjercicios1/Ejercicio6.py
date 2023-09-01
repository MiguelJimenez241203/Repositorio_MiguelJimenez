N=int(input("Ingrese un número: "))
print('Los divisores de',N, 'son:')
for divisor in range(1, N + 1):
    if N % divisor == 0:
        print(divisor)