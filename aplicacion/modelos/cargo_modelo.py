
from sqlalchemy import Column, Integer, String
from aplicacion.modelos.definicion import BaseCrud,db
class Cargo(BaseCrud,db.Model):
    __tablename__ = 'cargo'
    id_cargo = Column(Integer, primary_key=True, autoincrement=True)
    cargo = Column(String(255), nullable=False)