from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

enrutador = Blueprint('presentacion', __name__, url_prefix='/presentacion',template_folder='../vistas')

@enrutador.route('/index')
def pagina_index():
    try:
        return render_template("presentacion/index.html")
    except TemplateNotFound:
        abort(404)
