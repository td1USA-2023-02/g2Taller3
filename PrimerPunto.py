class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_stock(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        print(f"Stock de '{self.nombre}' actualizado a {nueva_cantidad}.")

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Stock: {self.cantidad}"

class Almacen:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.inventario[producto.nombre] = producto
            print(f"Producto '{producto.nombre}' agregado al almacén.")
        else:
            print("Error: El objeto no es de tipo Producto.")

    def mostrar_inventario(self):
        print("\nInventario del almacén:")
        for producto in self.inventario.values():
            print(producto)

# Profe este sería nuestro súper ejemplo
if __name__ == "__main__":
    
    almacen = Almacen()
    
    # Agregar nuestros súper productos al almacén
    almacen.agregar_producto(Producto("Laptop", 800, 10))
    almacen.agregar_producto(Producto("Mouse", 20, 50))
    
    
    almacen.mostrar_inventario()
    
    # Actualizar nuestro súper stock de un producto
    producto_laptop = almacen.inventario.get("Laptop")
    if producto_laptop:
        producto_laptop.actualizar_stock(8)
    
    
    almacen.mostrar_inventario()

