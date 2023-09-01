def numero_elementos(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * numero_elementos(n - 1)
    
def numero_muestras(n, m):
    return numero_elementos(n) // (numero_elementos(m) * numero_elementos(n - m))