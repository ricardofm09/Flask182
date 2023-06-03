class Bebida:
    def __init__(self, id, nombre, precio, clasificacion, marca):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.clasificacion = clasificacion
        self.marca = marca

class AlmacenBebidas:
    def __init__(self):
        self.bebidas = []

    def dar_de_alta(self, bebida):
        self.bebidas.append(bebida)
        print("Bebida agregada exitosamente.")

    def dar_de_baja(self, id):
        for bebida in self.bebidas:
            if bebida.id == id:
                self.bebidas.remove(bebida)
                print("Bebida eliminada exitosamente.")
                return
        print("No se encontró una bebida con el ID proporcionado.")

    def actualizar_producto(self, id, nombre, precio, clasificacion, marca):
        for bebida in self.bebidas:
            if bebida.id == id:
                bebida.nombre = nombre
                bebida.precio = precio
                bebida.clasificacion = clasificacion
                bebida.marca = marca
                print("Bebida actualizada exitosamente.")
                return
        print("No se encontró una bebida con el ID proporcionado.")

    def mostrar_bebidas(self):
        if len(self.bebidas) == 0:
            print("No hay bebidas en el almacén.")
        else:
            for bebida in self.bebidas:
                print("ID:", bebida.id)
                print("Nombre:", bebida.nombre)
                print("Precio:", bebida.precio)
                print("Clasificación:", bebida.clasificacion)
                print("Marca:", bebida.marca)
                print()

    def calcular_precio_promedio(self):
        if len(self.bebidas) == 0:
            print("No hay bebidas en el almacén.")
        else:
            total = 0
            for bebida in self.bebidas:
                total += bebida.precio
            precio_promedio = total / len(self.bebidas)
            print("El precio promedio de las bebidas es:", precio_promedio)

    def contar_bebidas_por_marca(self, marca):
        cantidad = 0
        for bebida in self.bebidas:
            if bebida.marca == marca:
                cantidad += 1
        print("Cantidad de bebidas de la marca", marca, ":", cantidad)

    def contar_bebidas_por_clasificacion(self, clasificacion):
        cantidad = 0
        for bebida in self.bebidas:
            if bebida.clasificacion == clasificacion:
                cantidad += 1
        print("Cantidad de bebidas de la clasificación", clasificacion, ":", cantidad)

# Función para mostrar el menú y obtener la opción seleccionada
def mostrar_menu():
    print("------ Menú ------")
    print("1. Dar de Alta una bebida")
    print("2. Dar de Baja una bebida")
    print("3. Actualizar una bebida")
    print("4. Mostrar todas las bebidas")
    print("5. Calcular precio promedio de las bebidas")
    print("6. Contar bebidas de una marca")
    print("7. Contar bebidas por clasificación")
    print("8. Salir")
    print()

    opcion = input("Selecciona una opción: ")
    return opcion

# Almacén de bebidas
almacen = AlmacenBebidas()

# Ciclo principal
while True:
    opcion = mostrar_menu()

    if opcion == "1":
        id = input("ID de la bebida: ")
        nombre = input("Nombre de la bebida: ")
        precio = float(input("Precio de la bebida: "))
        clasificacion = input("Clasificación de la bebida: ")
        marca = input("Marca de la bebida: ")
        bebida = Bebida(id, nombre, precio, clasificacion, marca)
        almacen.dar_de_alta(bebida)
        print()

    elif opcion == "2":
        id = input("ID de la bebida a eliminar: ")
        almacen.dar_de_baja(id)
        print()

    elif opcion == "3":
        id = input("ID de la bebida a actualizar: ")
        nombre = input("Nuevo nombre de la bebida: ")
        precio = float(input("Nuevo precio de la bebida: "))
        clasificacion = input("Nueva clasificación de la bebida: ")
        marca = input("Nueva marca de la bebida: ")
        almacen.actualizar_producto(id, nombre, precio, clasificacion, marca)
        print()

    elif opcion == "4":
        almacen.mostrar_bebidas()
        print()

    elif opcion == "5":
        almacen.calcular_precio_promedio()
        print()

    elif opcion == "6":
        marca = input("Marca de las bebidas a contar: ")
        almacen.contar_bebidas_por_marca(marca)
        print()

    elif opcion == "7":
        clasificacion = input("Clasificación de las bebidas a contar: ")
        almacen.contar_bebidas_por_clasificacion(clasificacion)
        print()

    elif opcion == "8":
        print("Hasta Pronto")
        break

    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
        print()
