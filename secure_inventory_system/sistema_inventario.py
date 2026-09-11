class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacio.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.nombre = nombre.strip()
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad: int):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio} | Cantidad: {self.cantidad} | Valor total: {self.calcular_valor_total()}"

class Inventario:
        def __init__(self):
            self.productos = []

        def agregar_producto(self, producto: Producto):
            self.productos.append(producto)

        def buscar_producto(self, nombre: str):
            nombre = nombre.strip().lower()
            for producto in self.productos:
                if producto.nombre.lower() == nombre:
                    return producto
            return None

        def calcular_valor_inventario(self):
            return sum(p.calcular_valor_total() for p in self.productos)

        def listar_productos(self):
            if not self.productos:
                print("No hay productos en el inventario.")
            else:
                for p in self.productos:
                    print(p)

def menu_principal(inventario: Inventario):
    while True:
        print("\n--- Sistema de Inventario ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))

                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("Producto agregado correctamente.")

            elif opcion == "2":
                nombre = input("Ingrese el nombre del producto a buscar: ")
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print("Producto encontrado: ")
                    print(producto)
                else:
                    print("Producto no encontrado: ")

            elif opcion == "3":
                inventario.listar_productos()

            elif opcion == "4":
                total = inventario.calcular_valor_inventario()
                print(f"Valor total del inventario: {total}")

            elif opcion == "5":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)
        