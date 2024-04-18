from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle,getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph,Spacer
from reportlab.lib.units import inch

import tempfile
import warnings
def javascript_alert(msg,pagina_destino=None):
    if pagina_destino == None:
        return f'''
            <script>
                alert("{msg}");
            </script>
            '''
    else:
        return f'''
            <script>
                alert("{msg}");
                window.location.href = "{pagina_destino}";
            </script>
            '''
def deprecated(message):
    def decorator(obj):
        if isinstance(obj, type):
            # Decorador aplicado a una clase
            class DeprecatedClass(obj):
                def __init__(self, *args, **kwargs):
                    warnings.warn(message, category=DeprecationWarning, stacklevel=2)
                    super().__init__(*args, **kwargs)
            return DeprecatedClass
        else:
            # Decorador aplicado a una función
            def new_func(*args, **kwargs):
                warnings.warn(message, category=DeprecationWarning, stacklevel=2)
                return obj(*args, **kwargs)
            return new_func
    return decorator
def generar_pdf(titulo_pdf,matriz_de_datos,anchos_de_columnas=[] ):
    # Creamos un objeto PDF usando reportlab
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    
    # Creamos un objeto PDF usando reportlab
    doc = SimpleDocTemplate(temp_file.name, pagesize=letter)
    elements = []
    # Agregamos un título al documento
    title_style = ParagraphStyle(name='TitleStyle', fontSize=20, alignment=1)
    title = Paragraph(titulo_pdf, title_style)
    elements.append(title)

    # Agregamos un espacio vertical entre el título y la tabla
    elements.append(Spacer(1, 20))  # Ajusta el valor 20 según sea necesario

    # Creamos las cabeceras de la tabla
    #data = [['id', 'razon social', 'nit / ci', 'estado'] ]
    # Llenamos de dato la tabla
    #for cliente in clientes:
    #    data.append([cliente.id_cliente, cliente.razon_social, cliente.nit_ci,cliente.estado ])
    estilos_de_tabla =TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey),
                               ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                               ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                               ('VALIGN', (0,0), (-1,-1), 'TOP'),
                               ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0,0), (-1,0), 12),
                               ('BACKGROUND', (0,1), (-1,-1), colors.white),
                               ('GRID', (0,0), (-1,-1), 1, colors.black)])
    

    # Obtener el estilo de párrafo predeterminado para las celdas que contienen cadenas largas
    styles = getSampleStyleSheet()
    paragraph_style = styles['Normal']
    # Recorrer la matriz de datos
    for fila in matriz_de_datos:
        for i, valor in enumerate(fila):
            if isinstance(valor, str) and len(valor) > 15:  # Verificar si el valor es una cadena y supera cierta longitud
                # Convertir la cadena en un objeto Paragraph
                fila[i] = Paragraph(valor, paragraph_style) 
    if len(anchos_de_columnas)>0 :        
        table = Table(matriz_de_datos, colWidths=anchos_de_columnas)
    else:
        table = Table(matriz_de_datos)
    table.setStyle(estilos_de_tabla)
    if len(anchos_de_columnas)>0 :
        table._colWidths = anchos_de_columnas
    # Calcular el ancho de la página
    page_width, page_height = letter
    table_width = page_width - 2 * 72  # Margen izquierdo y derecho de 1 pulgada (72 puntos)
    # table.wrapOn(doc, table_width, 0)
    # Añadimos la tabla al objeto PDF
    elements.append(table)

    # Construimos el PDF
    doc.build(elements)
    return temp_file