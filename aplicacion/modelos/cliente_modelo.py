
from sqlalchemy import Column, Integer, String
from aplicacion.modelos.definicion import BaseCrud,db

class Cliente(BaseCrud,db.Model):
    __tablename__ = 'cliente'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    razon_social = Column(String(255), nullable=False)
    nit_ci = Column(String(255), nullable=False)
    estado = Column(String(255), nullable=False)
    @classmethod
    def obtener_lista_activados(cls):
        try:
            return cls.query.filter_by(estado='activado' ).all()
        except Exception as e:
            print(e)
            return []
    @classmethod
    def obtener_lista_desactivados(cls):
        try:
            return cls.query.filter_by(estado='desactivado' ).all()
        except Exception as e:
            print(e)
            return []