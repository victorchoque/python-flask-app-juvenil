from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, CHAR, ForeignKey
from sqlalchemy.sql import  update

import logging
logging.basicConfig(level=logging.DEBUG)
db = SQLAlchemy()
class BaseCrud:
    __abstract__ = True
    def guardar(self):
        try:
            db.session.add(self)
            db.session.commit()
            print("Registro guardado exitosamente")
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    def editar(self):
        db.session.commit()
        return True
    
    def editar_no_funciona_como_debe(self, campos_de_diccionario_a_actualizar: dict):
        try:            
            for nombre_columna in self.__table__.columns.keys():
                if nombre_columna in campos_de_diccionario_a_actualizar:
                    setattr(self, nombre_columna, campos_de_diccionario_a_actualizar[nombre_columna])
            db.session.add(self)
            #db.session.commit()
            logging.debug("Antes de hacer commit")
            db.session.commit()
            logging.debug("Después de hacer commit")
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False

    #def editar(self, **kwargs):
    #    try:        
    #        for attr, value in kwargs.items():
    #            setattr(self, attr, value)
    #        db.session.merge(self)
    #        db.session.commit()
    #        return True
    #    except Exception as e:
    #        print(e)
    #        db.session.rollback()
    #        return False

    def borrar(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    @classmethod
    def obtener_lista(cls):
        try:
            return cls.query.all()
        except Exception as e:
            print(e)
            return []

    @classmethod
    def obtener(cls,  id_value):
        try:            
            return cls.query.get(id_value)
        except Exception as e:
            print(e)
            return None
    @classmethod
    def obtener_lista_clave_valor(cls, clave, valor):
        try:
            # Obtener todos los registros
            registros = cls.query.all()

            # Construir el diccionario asociativo usando los campos clave y valor especificados
            resultados = {}
            for registro in registros:
                clave_registro = getattr(registro, clave)
                valor_registro = getattr(registro, valor)
                resultados[clave_registro] = valor_registro
                
            return resultados
        except Exception as e:
            print(e)
            return {}
    


