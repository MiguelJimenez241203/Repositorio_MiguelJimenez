print('Bienvenido al programa de alimentos'.center(60,'-'))


lectura = open('Alimentos.txt','rt')
lineas = lectura.readlines()

CODIGO = []
DESCRIPCION = []
TARIFA_IVA_LEY_VIGENTE = []

for linea in lineas:
    columna = linea.strip().split(",")
    
    if len(columna) >= 3:
        codigos = columna[0]
        descripciones = columna[1]
        tarifas_iva = (columna[2])

        CODIGO.append(codigos)
        DESCRIPCION.append(descripciones)
        TARIFA_IVA_LEY_VIGENTE.append(tarifas_iva)

lectura.close()


while True:
    print("""
        (1) Ingresar el número de un producto
        (2) Salir del programa de alimentos
        """)
    
    respuesta = int(input('¿Qué opción va a elegir? '))

    if respuesta == 1:
        producto = (input('Ingrese algún producto del listado: '))
        
        if producto in DESCRIPCION:
            posicion_producto = DESCRIPCION.index(producto)
            posicion_iva = float(TARIFA_IVA_LEY_VIGENTE[posicion_producto])
            valor_neto = int(input('Ingrese el valor neto del producto: '))
            valor_iva=posicion_iva*100
            valor_base=valor_neto-valor_iva
            print(f'El valor base del producto es', valor_base, 'y el valor del iva fue ', valor_iva)
        else:
            print(f'El producto no está en la lista ')

    elif respuesta == 2:
        break


    