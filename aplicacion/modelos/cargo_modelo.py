
from sqlalchemy import Column, Integer, String
from aplicacion.modelos.definicion import BaseCrud,db
class Cargo(BaseCrud,db.Model):
    __tablename__ = 'cargo'
    id_cargo = Column(Integer, primary_key=True, autoincrement=True)
    cargo = Column(String(255), nullable=False)
    @classmethod
    def buscar_en_lista(cls,criterio):
        try:
            print(f'%{criterio}%')
            return cls.query \
                        .filter( cls.cargo.like(f'%{criterio}%') ) \
                        .all()
        except Exception as e:
            print(e)
            return []