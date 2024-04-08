from flask import Blueprint, render_template, request, redirect, url_for
from aplicacion.formularios import CargoForm  # Importa el formulario de Flask-WTF
from aplicacion.modelos.cargo_modelo import Cargo  # Importa la clase Cargo
from aplicacion.controladores.comun import javascript_alert

# Define el Blueprint
enrutador = Blueprint('cargo', __name__,url_prefix='/cargo',template_folder='../vistas')
# Ruta para agregar un nuevo cargo
@enrutador.route('/agregar', methods=['GET', 'POST'])
def agregar_cargo():
    script = None
    form = CargoForm(request.form)
    if request.method == 'POST' and form.validate():
        #nuevo_cargo = Cargo.guardar(cargo=form.cargo.data)
        nuevo_cargo = Cargo()
        nuevo_cargo.cargo = form.cargo.data
        if nuevo_cargo.guardar():
            # Redirige a la página de visualización de detalles del nuevo cargo
            #return redirect(url_for('cargo.listar_cargos', id=nuevo_cargo.id_cargo))
            # Genera el URL para la página a la que deseas redirigir
            pagina_destino = url_for('cargo.listar_cargos')
            # Crea el script JavaScript con la redirección
            script = javascript_alert("Cargo Agregado exitosamente",pagina_destino)
    return render_template('cargo/cargo_formulario.html', form=form,sub_titulo='Agregar Nuevo cargo',script=script)

# Ruta para editar un cargo existente
@enrutador.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cargo(id):
    script = None;
    cargo_modelo = Cargo.obtener(id)    
    if cargo_modelo is None:
        # Manejar caso donde no se encuentra el cargo_modelo
        pass
    print (cargo_modelo.id_cargo)
    form = CargoForm(request.form, obj=cargo_modelo)
    if request.method == 'POST' and form.validate():
        #cargo_modelo.update(id_cargo = id, cargo = form.cargo.data )
        #cargo_modelo.id_cargo = id
        cargo_modelo.cargo = form.cargo.data         
        # Redirige a la página de visualización de detalles del cargo editado
        #return redirect(url_for('cargo.ver_cargo', id=id))
        pagina_destino = url_for('cargo.listar_cargos')
        script =  javascript_alert("Un error no se pudo actualizar")
        if cargo_modelo.actualizar() :
            script =  javascript_alert("Se actualizo el cargo",pagina_destino)     
    return render_template('/cargo/cargo_formulario.html', form=form,sub_titulo='Editar cargo' + str(cargo_modelo.cargo), cargo=cargo_modelo,script=script)



# Ruta para borrar un cargo
@enrutador.route('/borrar/<int:id>', methods=['GET'])
def borrar_cargo(id):
    cargo = Cargo.obtener(id)
    pagina_destino = url_for('cargo.listar_cargos')
    script = None
    msg = 'Error no se pudo borrar'    
    if cargo is None :        
        # Crea el script JavaScript con la redirección
        None
    elif cargo.borrar():        
        msg = 'Cargo borrado exitosamente'    
    script = javascript_alert(msg,pagina_destino)
    #return redirect(url_for('cargo.listar_cargos'))
    return script

# Ruta para listar todos los cargos
@enrutador.route('/lista', methods=['GET', 'POST'])
@enrutador.route('/cargos')
def listar_cargos():
    cargos = Cargo.obtener_lista()
    return render_template('/cargo/cargo_lista.html', cargos_lista=cargos)
