class Producto:
    def __init__(self, nombre, precio, cantidad_disponible=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def obtener_info(self):
        return f"{self.nombre} - Precio: {self.precio} - Cantidad Disponible: {self.cantidad_disponible}"

    def restar_cantidad(self, cantidad):
        if cantidad > 0 and cantidad <= self.cantidad_disponible:
            self.cantidad_disponible -= cantidad
            return True
        else:
            return False

    def verificar_disponibilidad(self, cantidad):
        return cantidad <= self.cantidad_disponible


class Snack(Producto):
    def __init__(self, nombre, precio, cantidad_disponible, tipo_snack):
        super().__init__(nombre, precio, cantidad_disponible)
        self.tipo_snack = tipo_snack

    def obtener_info(self):
        return f"{super().obtener_info()} - Tipo de Snack: {self.tipo_snack}"


class Bebida(Producto):
    def __init__(self, nombre, precio, cantidad_disponible, tamaño_bebida):
        super().__init__(nombre, precio, cantidad_disponible)
        self.tamaño_bebida = tamaño_bebida

    def obtener_info(self):
        return f"{super().obtener_info()} - Tamaño de Bebida: {self.tamaño_bebida}"


class MaquinaDispensadora:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto and producto.verificar_disponibilidad(cantidad):
                producto.restar_cantidad(cantidad)
                return producto.precio * cantidad
        return 0

    def total_ventas(self):
        total = 0
        for producto in self.productos:
            total += (producto.precio * (producto.cantidad_disponible - producto.verificar_disponibilidad(0)))
        return total


snack1 = Snack("Galletas", 4.500, 12, "Dulce")
bebida1 = Bebida("Refresco", 6.000, 5, "Grande")

maquina = MaquinaDispensadora()
maquina.agregar_producto(snack1)
maquina.agregar_producto(bebida1)

print('----------------------------------------------------------------------------')
print(snack1.obtener_info())
print(bebida1.obtener_info())
print('----------------------------------------------------------------------------')
venta_total = maquina.realizar_venta("Galletas", 3)
print(f"Venta realizada. Total: ${venta_total:.2f}")
print('----------------------------------------------------------------------------')
print(snack1.obtener_info())
print(f"Total de ventas: ${maquina.total_ventas():.2f}")
print('----------------------------------------------------------------------------')