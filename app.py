from crypt import methods
import re
from wsgiref.util import request_uri
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Usuario, Producto, Venta, Detalle_venta
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

#RUTAS

#Consultar todo
@app.route('/usuario', methods=['GET'])
def getUsuario():
    usuario = Usuario.query.all()
    usuario = list(map(lambda x: x.serialize(), usuario))
    return jsonify(usuario), 200

#consultar usuario según id
@app.route('/usuario/<id>', methods=['GET'])
def getUsuario(id):
    usuario = Usuario.query.get(id)
    return jsonify(usuario.serialize()), 200

#borrar usuario según id
@app.route('/usuario/<id>', methods=['DELETE'])
def deleteUsuario(id):
    usuario = Usuario.query.get(id)
    Usuario.delete(usuario)
    return jsonify(usuario.serialize()), 200

#modificar usuario
@app.route('/usuario/<id>', methods=['PUT'])
def updateUsuario(id):
    usuario = Usuario.query.get(id)

    rut = request.json.get('rut')
    nombre = request.json.get('nombre')
    apellido = request.json.get('apellido')
    direccion = request.json.get('direccion')
    telefono = request.json.get('telefono')
    correo = request.json.get('correo')
    contrasenia = request.json.get('contrasenia')

    usuario.rut = rut
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.direccion = direccion
    usuario.telefono = telefono
    usuario.correo = correo
    usuario.contrasenia = contrasenia
    Usuario.save(usuario)

    return jsonify(usuario.serialize()), 200

#agregar usuario
@app.route('/usuario', methods = ['POST'])
def addUsuario(): 
    usuario = Usuario()
    rut = request.json.get('rut')
    nombre = request.json.get('nombre')
    apellido = request.json.get('apellido')
    direccion = request.json.get('direccion')
    telefono = request.json.get('telefono')
    correo = request.json.get('correo')
    contrasenia = request.json.get('contrasenia')

    usuario.rut = rut
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.direccion = direccion
    usuario.telefono = telefono
    usuario.correo = correo
    usuario.contrasenia = contrasenia
    Usuario.save(usuario)

    return jsonify(usuario.serialize()), 200

# 3. Creamos una ruta y debug=true para que el servidor se reinicie ante los cambios
# 4. añadimos un validador para saber si estamos ejecutando nuestra aplicacion
# 5. ejecutamos python app.py o python3 app.py
# 6. ejecutamos el comando flask db init
# 7. ejecutamos el comando flask db migrate
# 8. ejecutamos el comando flask db upgrade
# 9. ejecutamos el comando flask run --host=0.0.0.0 en caso que tengamos problemas con el cors

#consulta productos
@app.route('/productos', metohds = ['GET'])
def getProductos():
    producto = Producto.query.all()
    producto = list(map(lambda x: x.serialize(), producto))
    return jsonify(producto), 200

#consulta por un producto
@app.route('/productos/<id>', methods = ['GET'])
def getProducto(id):
    producto = Producto.query.get(id)
    return jsonify(producto.serialize()), 200

#borrar producto por id
@app.route('/productos/<id>', methods = ['DELETE'])
def deleteProducto(id):
    producto = Producto.query.get(id)
    Producto.delete(producto)
    return jsonify(producto.serialize()), 200

#modificar producto
@app.route('/productos/<id>', methods = ['PUT'])
def updateProducto(id):
    producto = Producto.query.get(id)

    codigo = request.json.get('codigo')
    nombre = request.json.get('nombre')
    valor = request.json.get('valor')
    stock = request.json.get('stock')
    descripcion = request.json.get('descripcion')
    imagen = request.json.get('imagen')

    producto.codigo = codigo
    producto.nombre = nombre
    producto.valor = valor
    producto.stock = stock
    producto.descripcion = descripcion
    producto.imagen = imagen
    Producto.save(producto)

    return jsonify(producto.serialize()),200

@app.route('/productos', methods = ['POST'])
def addProducto():
    producto = Producto.query.get(id)

    codigo = request.json.get('codigo')
    nombre = request.json.get('nombre')
    valor = request.json.get('valor')
    stock = request.json.get('stock')
    descripcion = request.json.get('descripcion')
    imagen = request.json.get('imagen')

    producto.codigo = codigo
    producto.nombre = nombre
    producto.valor = valor
    producto.stock = stock
    producto.descripcion = descripcion
    producto.imagen = imagen
    Producto.save(producto)

    return jsonify(producto.serialize()),200

    if __name__ == '__main__':
        app.run(port=3000, debug = True)

