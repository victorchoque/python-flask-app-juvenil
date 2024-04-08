from flask import Blueprint, render_template, request, redirect, url_for
from aplicacion.formularios import ClienteForm  # Importa el formulario de Flask-WTF
from aplicacion.modelos.cliente_modelo import Cliente  # Importa la clase clientepara llenar el desplegable
from aplicacion.controladores.comun import javascript_alert

# Define el Blueprint
enrutador = Blueprint('cliente', __name__,url_prefix='/cliente',template_folder='../vistas')

@enrutador.route('/agregar', methods=['GET', 'POST'])
def agregar_cliente():
    script = None
    form = ClienteForm(request.form)
    
    if request.method == 'POST' and form.validate():
        #nuevo_cliente = cliente.guardar(cliente=form.cliente.data)
        nuevo_cliente = Cliente()
        nuevo_cliente.razon_social = form.razon_social.data
        nuevo_cliente.nit_ci = form.nit_ci.data
        nuevo_cliente.estado = form.estado.data

        if nuevo_cliente.guardar():
            # Redirige a la página de visualización de detalles del nuevo cliente
            #return redirect(url_for('cliente.listar_clientes', id=nuevo_cliente.id_cliente))
            # Genera el URL para la página a la que deseas redirigir
            pagina_destino = url_for('cliente.listar_clientes')
            # Crea el script JavaScript con la redirección
            script = javascript_alert("cliente Agregado exitosamente",pagina_destino)
    return render_template('cliente/cliente_formulario.html', form=form,sub_titulo='Agregar Nuevo cliente',script=script)

# Ruta para editar un cliente existente
@enrutador.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    script = None;
    cliente_modelo = Cliente.obtener(id)    
    if cliente_modelo is None:
        # Manejar caso donde no se encuentra el cliente_modelo
        pass
    else:
        cliente_nombres = cliente_modelo.razon_social
    print (cliente_modelo.id_cliente)
    form = ClienteForm(request.form, obj=cliente_modelo)
    
    if request.method == 'POST' and form.validate():

        cliente_modelo.razon_social = form.razon_social.data
        cliente_modelo.nit_ci = form.nit_ci.data
        cliente_modelo.estado = form.estado.data
        
        # Redirige a la página de visualización de detalles del cliente editado
        #return redirect(url_for('cliente.ver_cliente', id=id))
        pagina_destino = url_for('cliente.listar_clientes')
        script =  javascript_alert("Un error no se pudo actualizar")
        if cliente_modelo.editar() :
            script =  javascript_alert("Se actualizo el cliente",pagina_destino)     
    return render_template('/cliente/cliente_formulario.html', form=form,sub_titulo='Editar cliente ' + str(cliente_nombres), cliente=cliente_modelo,script=script)



# Ruta para borrar un cliente
# Aplicamos el BORRADO LOGICO
@enrutador.route('/borrar/<int:id>', methods=['GET'])
def borrar_cliente(id):
    cliente = Cliente.obtener(id)
    pagina_destino = url_for('cliente.listar_clientes')
    script = None
    msg = 'Error no se pudo borrar'    
    if cliente is None :        
        # Crea el script JavaScript con la redirección
        None     
    else:
        cliente.estado = 'desactivado'
        if(cliente.editar()):
            msg = 'cliente borrado exitosamente'  
    #elif cliente.borrar():        
    #    msg = 'cliente borrado exitosamente'    
    
    script = javascript_alert(msg,pagina_destino)    
    return script

# Ruta para listar todos los clientes
@enrutador.route('/lista', methods=['GET', 'POST'])
def listar_clientes():
    clientes = Cliente.obtener_lista_activados()
    print(clientes)
    return render_template('/cliente/cliente_lista.html', clientes_lista=clientes)
@enrutador.route('/lista_desactivados', methods=['GET', 'POST'])
def listar_clientes_desactivados():
    clientes = Cliente.obtener_lista_desactivados()

    return render_template('/cliente/cliente_lista.html', clientes_lista=clientes)

    