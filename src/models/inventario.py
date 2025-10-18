class inventario:
    def __ini__(self):
        self.lista_productos = [];

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def eliminar_producto(self, indice):
        producto_eliminar = self.lista_productos[indice]
        self.lista_productos.remove(producto_eliminar)

    def mostar_productos(self):
        for producto in self.lista_productos:
            print(producto)
        