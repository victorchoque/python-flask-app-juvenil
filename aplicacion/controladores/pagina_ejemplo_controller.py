from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

enrutador = Blueprint('pagina_ejemplo', __name__, template_folder='templates')

@enrutador.route('/saludo')
def funcion_saludar(page):
    try:
        return "Hola este es un ejemplo"
    except TemplateNotFound:
        abort(404)
