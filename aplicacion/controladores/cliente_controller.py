from flask import Blueprint, render_template, request, redirect, url_for,make_response,send_file
from aplicacion.formularios import ClienteForm  # Importa el formulario de Flask-WTF
from aplicacion.modelos.cliente_modelo import Cliente  # Importa la clase clientepara llenar el desplegable
from aplicacion.controladores.comun import javascript_alert

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph,Spacer

import tempfile
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

@enrutador.route('/pdf_lista', methods=['GET', 'POST'])
def pdf_listar_clientes():
    clientes = Cliente.obtener_lista_activados()
    #print(clientes)
    # Creamos un objeto PDF usando reportlab
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    
    # Creamos un objeto PDF usando reportlab
    doc = SimpleDocTemplate(temp_file.name, pagesize=letter)
    elements = []
    # Agregamos un título al documento
    title_style = ParagraphStyle(name='TitleStyle', fontSize=20, alignment=1)
    title = Paragraph("Lista de Clientes", title_style)
    elements.append(title)

    # Agregamos un espacio vertical entre el título y la tabla
    elements.append(Spacer(1, 20))  # Ajusta el valor 20 según sea necesario

    # Creamos las cabeceras de la tabla
    data = [['id', 'razon social', 'nit / ci', 'estado'] ]
    # Llenamos de dato la tabla
    for cliente in clientes:
        data.append([cliente.id_cliente, cliente.razon_social, cliente.nit_ci,cliente.estado ])

    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey),
                               ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                               ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                               ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0,0), (-1,0), 12),
                               ('BACKGROUND', (0,1), (-1,-1), colors.beige),
                               ('GRID', (0,0), (-1,-1), 1, colors.black)]))

    # Añadimos la tabla al objeto PDF
    elements.append(table)

    # Construimos el PDF
    doc.build(elements)
    
    # Enviamos el archivo PDF como respuesta
    return send_file(temp_file.name, as_attachment=False, download_name='mi_pdf.pdf')
