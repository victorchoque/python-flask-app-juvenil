from flask import Blueprint, render_template, request, redirect, url_for,send_file
from aplicacion.formularios import EmpleadoForm  # Importa el formulario de Flask-WTF
from aplicacion.modelos.cargo_modelo import Cargo  # Importa la clase Empleado y cargo para llenar el desplegable
from aplicacion.modelos.empleado_modelo import Empleado
from aplicacion.controladores.comun import javascript_alert, generar_pdf

# Define el Blueprint
enrutador = Blueprint('empleado', __name__,url_prefix='/empleado',template_folder='../vistas')

@enrutador.route('/agregar', methods=['GET', 'POST'])
def agregar_empleado():
    script = None
    form = EmpleadoForm(request.form)
    form.id_cargo.choices = [(cargo.id_cargo, cargo.cargo) for cargo in Cargo.query.all()]    
    
    if request.method == 'POST' and form.validate():
        #nuevo_empleado = empleado.guardar(empleado=form.empleado.data)
        nuevo_empleado = Empleado()
        nuevo_empleado.ci = form.ci.data
        nuevo_empleado.nombre = form.nombre.data
        nuevo_empleado.paterno = form.paterno.data
        nuevo_empleado.materno = form.materno.data
        nuevo_empleado.direccion = form.direccion.data
        nuevo_empleado.telefono = form.telefono.data
        nuevo_empleado.fecha_nacimiento = form.fecha_nacimiento.data
        nuevo_empleado.genero = form.genero.data
        nuevo_empleado.intereses = form.intereses.data
        nuevo_empleado.id_cargo = form.id_cargo.data
        if nuevo_empleado.guardar():
            # Redirige a la página de visualización de detalles del nuevo empleado
            #return redirect(url_for('empleado.listar_empleados', id=nuevo_empleado.id_empleado))
            # Genera el URL para la página a la que deseas redirigir
            pagina_destino = url_for('empleado.listar_empleados')
            # Crea el script JavaScript con la redirección
            script = javascript_alert("empleado Agregado exitosamente",pagina_destino)
    return render_template('empleado/empleado_formulario.html', form=form,sub_titulo='Agregar Nuevo empleado',script=script)

# Ruta para editar un empleado existente
@enrutador.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_empleado(id):
    script = None;
    empleado_modelo = Empleado.obtener(id)    
    if empleado_modelo is None:
        # Manejar caso donde no se encuentra el empleado_modelo
        pass
    else:
        empleado_nombres = empleado_modelo.nombre + " "+ empleado_modelo.paterno
    print (empleado_modelo.id_empleado)
    form = EmpleadoForm(request.form, obj=empleado_modelo)
    form.id_cargo.choices = [(cargo.id_cargo, cargo.cargo) for cargo in Cargo.query.all()] 
    if request.method == 'POST' and form.validate():
        #empleado_modelo.update(id_empleado = id, empleado = form.empleado.data )
        #empleado_modelo.id_empleado = id
        empleado_modelo.ci = form.ci.data
        empleado_modelo.nombre = form.nombre.data
        empleado_modelo.paterno = form.paterno.data
        empleado_modelo.materno = form.materno.data
        empleado_modelo.direccion = form.direccion.data
        empleado_modelo.telefono = form.telefono.data
        empleado_modelo.fecha_nacimiento = form.fecha_nacimiento.data
        empleado_modelo.genero = form.genero.data
        empleado_modelo.intereses = form.intereses.data
        empleado_modelo.id_cargo = form.id_cargo.data

        # Redirige a la página de visualización de detalles del empleado editado
        #return redirect(url_for('empleado.ver_empleado', id=id))
        pagina_destino = url_for('empleado.listar_empleados')
        script =  javascript_alert("Un error no se pudo actualizar")
        if empleado_modelo.editar() :
            script =  javascript_alert("Se actualizo el empleado",pagina_destino)     
    return render_template('/empleado/empleado_formulario.html', form=form,sub_titulo='Editar empleado ' + str(empleado_nombres), empleado=empleado_modelo,script=script)



# Ruta para borrar un empleado
@enrutador.route('/borrar/<int:id>', methods=['GET'])
def borrar_empleado(id):
    empleado = Empleado.obtener(id)
    pagina_destino = url_for('empleado.listar_empleados')
    script = None
    msg = 'Error no se pudo borrar'    
    if empleado is None :        
        # Crea el script JavaScript con la redirección
        None
    elif empleado.borrar():        
        msg = 'empleado borrado exitosamente'    
    script = javascript_alert(msg,pagina_destino)
    #return redirect(url_for('empleado.listar_empleados'))
    return script

# Ruta para listar todos los empleados
@enrutador.route('/lista', methods=['GET', 'POST'])
def listar_empleados():
    if request.args.get('buscar') != None and len( request.args.get('buscar') )>0:
        empleados = Empleado.buscar_en_lista( request.args.get('buscar') )
    else:
        empleados = Empleado.obtener_lista()
    return render_template('/empleado/empleado_lista.html', empleados_lista=empleados,con_busqueda=True)

@enrutador.route('/pdf_lista', methods=['GET', 'POST'])
def pdf_listar():
    empleados = Empleado.obtener_lista()
    
    datos = [['id', 'cargo','ci', 'Nombres', 'direccion','telefono','fecha nacimiento','genero','intereses'] ]
    #ancho = [  10,   10   , 10,50       ,100         ,11        ,100               ,100     ,100       ]
    ancho=[]
    # Llenamos de dato la tabla
    for empleado in empleados:
        datos.append([
                    empleado.id_empleado, 
                    empleado.cargo.cargo,
                    empleado.ci, 

                    "".join( [empleado.nombre," ",empleado.paterno," ",empleado.materno])  ,
                    empleado.direccion,
                    empleado.telefono,                    
                    empleado.fecha_nacimiento,
                    empleado.genero,
                    empleado.intereses.replace(",",", "),                    
                    ])        
    
    archivo_pdf = generar_pdf("Reporte Empleados",datos,ancho)
    
    # Enviamos el archivo PDF como respuesta
    return send_file(archivo_pdf.name, as_attachment=False, download_name='mi_pdf.pdf')