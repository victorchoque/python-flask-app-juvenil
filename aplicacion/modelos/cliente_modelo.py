
from sqlalchemy import Column, Integer, String, or_
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
    @classmethod
    def buscar_en_lista(cls,criterio):
        try:
            print(f'%{criterio}%')
            return cls.query.filter_by(estado='activado') \
                        .filter(or_(cls.razon_social.like(f'%{criterio}%'), cls.nit_ci.like(f'%{criterio}%'))) \
                        .all()
        except Exception as e:
            print(e)
            return []