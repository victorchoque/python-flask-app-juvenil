
from sqlalchemy import Column, Integer, String, Date, CHAR, ForeignKey,or_
from aplicacion.modelos.definicion import BaseCrud,db
from sqlalchemy.orm import relationship
class Empleado(BaseCrud,db.Model):
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
    @classmethod
    def buscar_en_lista(cls,criterio):
        try:
            print(f'%{criterio}%')
            return cls.query \
                            .filter(or_(cls.nombre.like(f'{criterio}%'),  
                                        cls.paterno.like(f'{criterio}%'),
                                        cls.materno.like(f'{criterio}%'),
                                        cls.ci.like(f'{criterio}%'),                                        
                                        )) \
                            .all()
        except Exception as e:
            print(e)
            return []