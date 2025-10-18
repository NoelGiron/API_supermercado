class producto:
    def __init__(self, nombre, categoria, descripcion, precio, cantidad, vencimineto):
        self.nombre = nombre
        self.categoria = categoria
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.vencimiento = vencimineto

def to_dict(self):
        """Convierte el objeto producto a diccionario para JSON"""
        return {
            'nombre': self.nombre,
            'categoria': self.categoria,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'cantidad': self.cantidad,
            'vencimiento': self.vencimiento
        }