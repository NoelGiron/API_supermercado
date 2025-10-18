import os
from models.producto import producto
from models.inventario import inventario

from flask import Blueprint, json, jsonify, request

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
    
    archivo_json = 'database/inventario.json'
    if os.path.exists(archivo_json) and os.path.getsize(archivo_json) > 0:
        with open(archivo_json, 'r', encoding='utf-8') as file:
            productos_data = json.load(file)

            for producto_data in productos_data:
                producto_existente = producto(
                        producto_data['nombre'],
                        producto_data['categoria'],
                        producto_data['descripcion'],
                        producto_data['precio'],
                        producto_data['cantidad'],
                        producto_data['vencimiento']
                )
                nuevo_inventario.agregar_producto(producto_existente)

        nuevo_inventario.agregar_producto(nuevo_producto)

        productos_para_json = [prod.to_dict() for prod in nuevo_inventario.lista_productos]

        with open(archivo_json, 'w', encoding='utf-8') as file:
            json.dump(productos_para_json, file, indent=4, ensure_ascii=False)

    return {'producto': nuevo_producto.to_dict}

@funciones_bp.route('/productos/lista', methods=['GET'])
def listar_productos():
        
        archivo_json = 'database/inventario.json'  
        if not os.path.exists(archivo_json) or os.path.getsize(archivo_json) == 0:
            return jsonify({
                'mensaje': 'No hay productos en el inventario',
                'productos': []
            })

        with open(archivo_json, 'r', encoding='utf-8') as file:
            productos = json.load(file)

        return jsonify({
            'total_productos': len(productos),
            'productos': productos
        })

@funciones_bp.route('/usuarios/eliminar')
def eliminar_producto(indice):

    archivo_json = 'database/inventario.json'
        
    if not os.path.exists(archivo_json):
        return jsonify({'error': 'No existe el archivo de inventario'}), 404
    
    with open(archivo_json, 'r', encoding='utf-8') as file:
        productos = json.load(file)
    
    if indice < 0 or indice >= len(productos):
        return jsonify({
            'error': f'Índice {indice} fuera de rango. Hay {len(productos)} productos'
        })
    
    producto_eliminado = productos[indice]
    
    producto_eliminado = productos.pop(indice)
    
    with open(archivo_json, 'w', encoding='utf-8') as file:
        json.dump(productos, file, indent=4, ensure_ascii=False)
    
    return jsonify({
        'mensaje': 'Producto eliminado exitosamente',
        'producto_eliminado': producto_eliminado,
        'total_productos_restantes': len(productos)
    })
    return

