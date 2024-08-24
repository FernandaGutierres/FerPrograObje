
# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def a_cadena(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_cadena(product_str):
        id_producto, nombre, cantidad, precio = product_str.split(',')
        return Producto(id_producto, nombre, int(cantidad), float(precio))

# Clase Inventario
class Inventario:
    def __init__(self, archivo):
        self.archivo = archivo

    def añadir_producto(self, producto):
        if self.mostrar_producto_por_id(producto.id_producto):
            return False
        with open(self.archivo, 'a') as f:
            f.write(producto.a_cadena() + '\n')
        return True

    def eliminar_producto(self, id_producto):
        productos = self.leer_productos()
        productos_actualizados = [p for p in productos if p.id_producto != id_producto]
        if len(productos_actualizados) < len(productos):
            self.guardar_productos(productos_actualizados)
            return True
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        productos = self.leer_productos()
        for p in productos:
            if p.id_producto == id_producto:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                self.guardar_productos(productos)
                return True
        return False

    def buscar_producto(self, nombre):
        productos = self.leer_productos()
        resultados = [p for p in productos if nombre.lower() in p.nombre.lower()]
        return resultados

    def mostrar_producto_por_id(self, id_producto):
        productos = self.leer_productos()
        for p in productos:
            if p.id_producto == id_producto:
                return p
        return None

    def mostrar_productos(self):
        return self.leer_productos()

    def leer_productos(self):
        productos = []
        with open(self.archivo, 'r') as f:
            for line in f:
                productos.append(Producto.from_cadena(line.strip()))
        return productos

    def guardar_productos(self, productos):
        with open(self.archivo, 'w') as f:
            for p in productos:
                f.write(p.a_cadena() + '\n')

# Clase para administrar el inventario desde la consola
class AdministrarTienda:
    def __init__(self, archivo):
        self.inventario = Inventario(archivo)
        self.menu_principal()

    def menu_principal(self):
        while True:
            print("\n--- MOVIMIENTOS DE TIENDA ---")
            print("1. Añadir producto")
            print("2. Buscar producto")
            print("3. Eliminar producto")
            print("4. Mostrar todos los productos")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.ingreso_productos()
            elif opcion == "2":
                self.formulario_busqueda_producto()
            elif opcion == "3":
                self.formulario_eliminar_producto()
            elif opcion == "4":
                self.mostrar_todos_los_productos()
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

    def ingreso_productos(self):
        id_producto = input("ID Producto: ")
        nombre_producto = input("Nombre: ")
        cantidad_producto = input("Cantidad: ")
        precio_producto = input("Precio: ")

        if not all([id_producto, nombre_producto, cantidad_producto, precio_producto]):
            print("Advertencia: Todos los campos deben ser completados.")
            return

        producto_existente = self.inventario.mostrar_producto_por_id(id_producto)
        if producto_existente:
            producto_existente.nombre = nombre_producto
            producto_existente.cantidad = int(cantidad_producto)
            producto_existente.precio = float(precio_producto)
            self.inventario.actualizar_producto(id_producto, producto_existente.cantidad, producto_existente.precio)
            print("Producto actualizado correctamente.")
        else:
            producto = Producto(id_producto, nombre_producto, int(cantidad_producto), float(precio_producto))
            if self.inventario.añadir_producto(producto):
                print("Producto añadido correctamente.")
            else:
                print("Error: ID del producto ya existe.")

    def formulario_busqueda_producto(self):
        nombre = input("Nombre del producto a buscar: ")
        resultados = self.inventario.buscar_producto(nombre)
        if resultados:
            for p in resultados:
                print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
        else:
            print("No se encontraron productos.")

    def formulario_eliminar_producto(self):
        id_producto = input("ID del producto a eliminar: ")
        if self.inventario.eliminar_producto(id_producto):
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_todos_los_productos(self):
        productos = self.inventario.mostrar_productos()
        if productos:
            for p in productos:
                print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
        else:
            print("No hay productos en el inventario.")

# Ejecutar la aplicación
if __name__ == "__main__":
    archivo_inventario = "inventario.txt"
    AdministrarTienda(archivo_inventario)