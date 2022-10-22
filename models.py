import re
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Region(db.Model):
    __tablename__ ='Region'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250), nullable = False)


class Comuna(db.Model):
    __tablename__ = 'Comuna'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250), nullable = False)

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key = True)
    rut = db.Column(db.Integer, unique = True, nullable = False)
    nombre = db.Column(db.String(250), nullable= False)
    apellido = db.Column(db.String(250), nullable = False)
    direccion = db.Column(db.string(250), nullable = False)
    telefono = db.Column(db.Integer, nullable = False)
    correo = db.Column(db.String(250), nullable = False)
    contrasenia = db.Column(db.String(250), nullable = False)

    def serialize(self):
        return {
            "id": self.id,
            "rut": self.rut,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "correo": self.correo,
            "contrasenia": self.contrasenia
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete
        db.session.commit()

class Producto(db.Model):
    __tablename__= 'Producto'
    id = db.Column(db.Integer, primary_key = True)
    codigo = db.Column(db.Integer, nullable = False)
    nombre = db.Column(db.String(250), nullable = False)
    valor = db.Column(db.Integer, nullable = False)
    stock = db.Column(db.Integer, nullable = False)
    descripcion = db.Column(db.String(250), nullable = False)
    imagen = db.Column(db.String(250), nullable = True)

    def serialize(self):
        return{
            "id": self.id,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "stock": self.stock,
            "descripcion": self.descripcion,
            "imagen": self.imagen
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Detalle_venta(db.Model):
    __tablename__ = 'Detalle_venta'
    id = db.Column(db.Integer, primary_key = True)
    cantidad = db.Column(db.Integer, nullable = False)
    valor = db.Column(db.Integer, nullable = False)
    descuento = db.Column(db.Integer, nullable = True)

class Venta(db.Model):
    __tablename__ = 'Venta'
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, nullable = False)
    descuento = db.Column(db.Integer, nullable = True)
    sub_total = db.Column(db.Integer, nullable = False)
    iva = db.Column(db.Integer, nullable = False)
    total = db.Column(db.Integer, nullable = False)

