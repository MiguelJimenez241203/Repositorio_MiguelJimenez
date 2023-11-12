class Articulo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio_bruto(self):
        pass


class AlimentoExento(Articulo):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.iva = 0

    def calcular_precio_bruto(self):
        valor_iva = self.precio * self.iva
        valor_base = self.precio - valor_iva
        return valor_base, valor_iva


class Alimento5Porciento(Articulo):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.iva = 0.05

    def calcular_precio_bruto(self):
        valor_iva = self.precio * self.iva
        valor_base = self.precio - valor_iva
        return valor_base, valor_iva


class Alimento19Porciento(Articulo):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.iva = 0.19

    def calcular_precio_bruto(self):
        valor_iva = self.precio * self.iva
        valor_base = self.precio - valor_iva
        return valor_base, valor_iva


print('Bienvenido al programa de alimentos'.center(60, '-'))

lectura = open('Alimentos.txt', 'rt')
lineas = lectura.readlines()

CODIGO = []
DESCRIPCION = []
TARIFA_IVA_LEY_VIGENTE = []

for linea in lineas:
    columna = linea.strip().split(",")

    if len(columna) >= 3:
        codigos = columna[0]
        descripciones = columna[1]
        tarifas_iva = float(columna[2])

        CODIGO.append(codigos)
        DESCRIPCION.append(descripciones)
        TARIFA_IVA_LEY_VIGENTE.append(tarifas_iva)

lectura.close()

alimentos = []
for i in range(len(CODIGO)):
    if float(TARIFA_IVA_LEY_VIGENTE[i]) == 0:
        alimentos.append(AlimentoExento(DESCRIPCION[i], 0))
    elif float(TARIFA_IVA_LEY_VIGENTE[i]) == 0.05:
        alimentos.append(Alimento5Porciento(DESCRIPCION[i], 0))
    elif float(TARIFA_IVA_LEY_VIGENTE[i]) == 0.19:
        alimentos.append(Alimento19Porciento(DESCRIPCION[i], 0))

while True:
    print("""
        (1) Ingresar el número de un producto
        (2) Salir del programa de alimentos
        """)

    respuesta = int(input('¿Qué opción va a elegir? '))

    if respuesta == 1:
        producto = input('Ingrese algún producto del listado: ')
        if producto in DESCRIPCION:
            posicion_producto = DESCRIPCION.index(producto)
            valor_neto = float(input('Ingrese el valor neto del producto: '))
            alimentos[posicion_producto].precio = valor_neto
            valor_base, valor_iva = alimentos[posicion_producto].calcular_precio_bruto()
            print(f'El valor base del producto es {valor_base} y el valor del IVA fue {valor_iva}')

        else:
            print('El producto no está en la lista ')

    elif respuesta == 2:
        break