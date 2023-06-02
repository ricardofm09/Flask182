class Bebida:
    def __init__(self, id, nombre, precio, marca, clasificacion):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.clasificacion = clasificacion


class AlmacenBebidas:
    def __init__(self):
        self.bebidas = []

    def alta_bebida(self, bebida):
        self.bebidas.append(bebida)

    def baja_bebida(self, id):
        self.bebidas = [bebida for bebida in self.bebidas if bebida.id != id]

    def actualizar_bebida(self, id, nombre, clasificacion, marca, precio):
        for bebida in self.bebidas:
            if bebida.id == id:
                bebida.nombre = nombre
                bebida.clasificacion = clasificacion
                bebida.marca = marca
                bebida.precio = precio
                break

    def mostrar_bebidas(self):
        for bebida in self.bebidas:
            print(f"ID: {bebida.id}")
            print(f"Nombre: {bebida.nombre}")
            print(f"Clasificación: {bebida.clasificacion}")
            print(f"Marca: {bebida.marca}")
            print(f"Precio: {bebida.precio}")
            print("---------------------------")

    def precio_promedio_bebidas(self):
        total_precios = sum(bebida.precio for bebida in self.bebidas)
        promedio = total_precios / len(self.bebidas)
        return promedio

    def cantidad_bebidas_marca(self, marca):
        cantidad = sum(1 for bebida in self.bebidas if bebida.marca == marca)
        return cantidad

    def cantidad_por_clasificacion(self, clasificacion):
        cantidad = sum(1 for bebida in self.bebidas if bebida.clasificacion == clasificacion)
        return cantidad


# Ejemplo de uso
almacen = AlmacenBebidas()

bebida1 = Bebida(1, "Agua Mineral", "Agua", "MarcaA", 1.5)
bebida2 = Bebida(2, "Refresco de Cola", "Bebida Azucarada", "MarcaB", 2.0)
bebida3 = Bebida(3, "Bebida Energética", "Bebida Energética", "MarcaA", 3.5)

almacen.alta_bebida(bebida1)
almacen.alta_bebida(bebida2)
almacen.alta_bebida(bebida3)

almacen.mostrar_bebidas()

almacen.baja_bebida(2)

almacen.actualizar_bebida(1, "Agua Mineral con Gas", "Agua", "MarcaA", 2.0)

almacen.mostrar_bebidas()

promedio = almacen.precio_promedio_bebidas()
print(f"Precio promedio de bebidas: {promedio}")

cantidad_marca = almacen.cantidad_bebidas_marca("MarcaA")
print(f"Cantidad de bebidas de MarcaA: {cantidad_marca}")

cantidad_clasificacion = almacen.cantidad_por_clasificacion("Bebida Energética")
print(f"Cantidad de bebidas de clasificación 'Bebida Energética': {cantidad_clasificacion}")
