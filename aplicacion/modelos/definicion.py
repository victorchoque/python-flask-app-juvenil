from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, CHAR, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Cargo(db.Model):
    __tablename__ = 'cargo'
    id_cargo = Column(Integer, primary_key=True, autoincrement=True)
    cargo = Column(String(255), nullable=False)

class Empleado(db.Model):
    __tablename__ = 'empleado'
    id_empleado = Column(Integer, primary_key=True, autoincrement=True)
    ci = Column(String(255), nullable=False)
    nombre = Column(String(255), nullable=False)
    paterno = Column(String(255), nullable=False)
    materno = Column(String(255), nullable=False)
    direccion = Column(String(255), nullable=False)
    telefono = Column(Integer, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    genero = Column(CHAR(2), nullable=False)
    intereses = Column(String(120), nullable=False)
    id_cargo = Column(Integer, ForeignKey('cargo.id_cargo'), nullable=False)
    cargo = relationship("Cargo", backref="empleados")

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    razon_social = Column(String(255), nullable=False)
    nit_ci = Column(String(255), nullable=False)
    estado = Column(String(255), nullable=False)
