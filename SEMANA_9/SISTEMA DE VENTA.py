class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id=id
        self.nombre=nombre
        self.cantidad=cantidad
        self.precio=precio

        #metodos geetters
        # Métodos Getters para acceder y modificar los atributos
        def get_id(self):
            return self.id

        def get_nombre(self):
            return self.nombre

        def get_cantidad(self):
            return self.cantidad

        def get_precio(self):
            return self.precio

        # Métodos Setters para acceder y modificar los atributos
        def set_id(self, id):
            self.id = id

        def set_nombre(self, nombre):
            self.nombre = nombre

        def set_cantidad(self, cantidad):
            self.cantidad = cantidad

        def set_precio(self, precio):
            self.precio = precio

        def __str__(self):
            return f'ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}'

        class Inventario:
            def __init__(self):
                self.productos = []

            def añadir_productos(self, producto):
                for p in self.productos:
                    if p.get_id() == producto.get.id():
                        print("Error el ad de prodiccto ya existe")
                        return
                self.productos.append(producto)
                print("El producto se anadio exitosamente")

            def eliminar_producto(self, id):
                for p in self.productos:
                    if p.get_id ()==id:
                        self.productos.remove(p)
                        print("el producto fue eliminado existosamente")
                        return
                    print("No existe el producto")

            def actualizar_producto(self, id):

            def buscar_producto(self,id ):


            def mostrar_productos(self,  id ):