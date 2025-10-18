from models.producto import producto
from models.inventario import inventario

from flask import Blueprint, request

nuevo_inventario = inventario()

funciones_bp = Blueprint('productos', __name__)

@funciones_bp.route('/productos/crear', methods=['POST'])
def crear_producto():
    data = request.get_json()

    nombre = data['nombre']
    categoria = data['categoria']
    descripcion = data['descripcion']
    precio = data['precio']
    cantidad = data['cantidad']
    vencimiento = data['vencimiento']

    nuevo_producto = producto(nombre, categoria, descripcion, precio, cantidad, vencimiento)
    nuevo_inventario.agregar_producto(nuevo_producto)

    return {'mensaje': 'el producto se a agregado al inventario'}

@funciones_bp.route('/productos/lista')
def mostrar_inventario():
    inventario
    return {'mensaje': 'Lista de productos'}

@funciones_bp.route('/usuarios/eliminar')
def obtener_usuario(id):
    return {'mensaje': f'Usuario {id}'}

