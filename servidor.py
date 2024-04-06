# Las clases de "Blueprint" sirven para agrupar archivos python y sacar los get,post definidos en ellos
from flask import Blueprint, render_template, abort,redirect, url_for
from flask import Flask
# Importamos las definiciones de base de datos

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from aplicacion.modelos.definicion import db


# importamos todos los controladores
from aplicacion.controladores import pagina_ejemplo_controller, presentacion_controller


#app = Flask(__name__, static_folder='/assets', static_url_path='/assets')
servidor = Flask(__name__)

servidor.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///juvenil.db'  # Usa SQLite como tu base de datos
servidor.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(servidor)
migrate = Migrate(servidor, db)

servidor.register_blueprint(presentacion_controller.enrutador)
servidor.register_blueprint(pagina_ejemplo_controller.enrutador)

#@servidor.route('/', defaults={'page': 'presentacion/index'})
@servidor.route('/')
def index():
    return redirect(url_for('presentacion.pagina_index'))
    #return 'Web servidor with Python Flask!'

servidor.run(host='0.0.0.0', port=8080,debug=True)