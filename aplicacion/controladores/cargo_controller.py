from flask import Blueprint, render_template, request, redirect, url_for ,send_file
from aplicacion.formularios import CargoForm  # Importa el formulario de Flask-WTF
from aplicacion.modelos.cargo_modelo import Cargo  # Importa la clase Cargo
from aplicacion.controladores.comun import javascript_alert,generar_pdf

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
    if request.args.get('buscar') != None and len( request.args.get('buscar') )>0:
        cargos = Cargo.buscar_en_lista( request.args.get('buscar') )
    else:
        cargos = Cargo.obtener_lista()
    return render_template('/cargo/cargo_lista.html', cargos_lista=cargos, con_busqueda=True)

# Ruta para generar el reporte
@enrutador.route('/pdf_lista', methods=['GET', 'POST'])
def pdf_listar():
    cargos = Cargo.obtener_lista()
    
    datos = [['id', 'Cargo'] ]
    # Llenamos de dato la tabla
    for cargo in cargos:
        datos.append([cargo.id_cargo, cargo.cargo ])
    
    archivo_pdf = generar_pdf("Reporte Cargos",datos)
    
    # Enviamos el archivo PDF como respuesta
    return send_file(archivo_pdf.name, as_attachment=False, download_name='mi_pdf.pdf')
