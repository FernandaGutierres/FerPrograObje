"""Desarrollar un sistema avanzado de gestión de inventarios para una tienda,
 que incorpore las colecciones en POO para un manejo eficiente de los ítems del inventario y
  almacene la información del inventario en archivos."""

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre =nombre
        self.cantidad = cantidad
        self.precio= precio

        def __str__(self):
            return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

        def obtener_id(self):
            return self.id_producto

        def obtener_nombre(self):
            return self.nombre

        def establecer_nombre(self, nombre):
            self.nombre = nombre

        def obtener_cantidad(self):
            return self.cantidad

        def establecer_cantidad(self, cantidad):
            self.cantidad = cantidad

        def obtener_precio(self):
            return self.precio

        def establecer_precio(self, precio):
            self.precio = precio
            
