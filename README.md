~~Para esta documnentacion se recomienda tener un minimo de conocimiento con respecto a los archivos MD o Markdown para la jerarquia sea clara~~(Mejorado con GPT)

Para esta documentación, se recomienda tener un mínimo de conocimiento sobre archivos MD o Markdown para garantizar que la jerarquía sea clara y se pueda aprovechar al máximo la estructura y formato proporcionados por este tipo de documentos.
# 1 python-flask-app-juvenil

## 1.1 Para Hacer Ejecutar el proyecto
escribir el comando
```bash
python servidor.py
```
recuerda instalar  [sus dependecias ](#2-instalar-python-con-flask--flask-sqlalchemy--flask-migrate--flask-wtf-y-reportlab) si es la primera vez con

## 1.3 Componentes/Librerias python usadas
- **Flask**: Flask es un framework de desarrollo web en Python que facilita la creación de aplicaciones web de forma rápida y sencilla. Es conocido por ser ligero y flexible, permitiendo a los desarrolladores construir aplicaciones web desde simples páginas estáticas hasta aplicaciones complejas con API RESTful.

- **Flask.Blueprint**: Flask.Blueprint es una característica de Flask que permite organizar y estructurar una aplicación web en módulos reutilizables y escalables. Los blueprints son útiles para dividir una aplicación en componentes más pequeños y manejables, lo que facilita el mantenimiento y la colaboración en proyectos grandes.

- **Flask-SQLAlchemy**:Flask-SQLAlchemy es una extensión de Flask que proporciona una integración sencilla entre Flask y SQLAlchemy, un popular ORM (Mapeo Objeto-Relacional) para Python. Flask-SQLAlchemy simplifica la configuración y el uso de SQLAlchemy en aplicaciones Flask, permitiendo a los desarrolladores trabajar con bases de datos de manera más eficiente y fácilmente.

- **Flask.Migrate**: Flask-Migrate es una extensión de Flask que proporciona herramientas para gestionar y realizar migraciones de base de datos de manera sencilla y segura. Las migraciones de base de datos son cambios en la estructura de la base de datos que deben aplicarse de manera coherente a lo largo del tiempo, y Flask-Migrate simplifica este proceso al automatizar la generación y aplicación de scripts de migración.

- **Flask-WTF**:Flask-WTF es una extensión de Flask que proporciona integración con la biblioteca WTForms, que facilita la creación y validación de formularios en aplicaciones web Flask. Flask-WTF simplifica la creación de formularios HTML y el manejo de datos de formulario en las vistas de Flask, ayudando a los desarrolladores a construir formularios seguros y fáciles de usar con facilidad.

- **reportlab**: Para crear PDF y crear reportes en PDF

## 1.3 Metodologia KANBAN para desarrollo este proyecto
### 1.3.1 Descripcion
Implementamos la metodología KANBAN para el desarrollo de este proyecto, el cual es de pequeña escala y tiene como objetivo servir como una demostración. En el equipo participan 4 personas, incluyendo un freelancer y tres pasantes. KANBAN nos permite gestionar las tareas de forma eficiente, visualizando el flujo de trabajo y priorizando las actividades según las necesidades del proyecto. Esta metodología nos ayuda a mantenernos organizados, colaborar de manera efectiva y realizar un seguimiento claro del progreso en todas las etapas del desarrollo


## 1.4 Herramientas externas usadas
- **ChatGPT**: Utilizamos ChatGPT para resolver dudas puntuales sobre funciones y ejemplos de programación.
- **Copilot**: Empleamos Copilot para agilizar el autocompletado de funciones rutinarias. Se recomienda su uso solo para aquellos con un nivel medio-avanzado en programación, capaces de distinguir versiones y estructuras.
- **VSCode**: Utilizamos Visual Studio Code como nuestro editor principal, que además es gratuito.
- **Git**: Utilizamos Git como sistema de gestión de versiones para controlar el desarrollo del proyecto y colaborar de manera eficiente.
- **GitHub**: Utilizamos GitHub, que nos brinda la posibilidad de utilizar Kanban para organizar y gestionar nuestras tareas de manera efectiva.
- **VSCode:alexcvzz.vscode-sqlite** : plugin para Vscode, para realizar consultas y ver la informacion que esta almacenada en la base de datos de SQLITE para hacer verificaciones constantes de si: edita,borra,lista o filtra las Querys

# 2 Instalar python con Flask , Flask-SQLAlchemy , Flask-Migrate , Flask-WTF y reportlab
- WINDOWS, link de descarga de Python https://www.python.org/downloads/release/python-3123/
- Debes de tener instalado Python 3 (por DEFAULT instala el comando "PIP")
- descargar este repositorio como ZIP
- Ir a la carpeta
- ejecutar comando "pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-WTF reportlab"
```bash
cd c:\proyectos\RutaDeEstaCarpeta\
pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-WTF reportlab
```
**Para instalacion OFFLINE EN WINDOWS**
```bash
cd c:\proyectos\RutaDeEstaCarpeta\
pip install -r requirements.txt --find-links=c:\proyectos\RutaDeEstaCarpeta\paquetes-externos\win64 --no-index
```
## [2.1](#2-1) Base de datos y ¿Migraciones? 
En este apartado, se abstraen las tablas necesarias y se normalizan los nombres de los campos para facilitar su uso en una base de datos MySQL, PostgreSQL o SQLite. Una vez hecho esto, se procede a migrar dicha abstracción al gestor de base de datos elegido.
### 2.1.1 Normalizacion de la estructura  de la base de datos y las abstracciones
- en Python una "tabla" se representara en una clase con el nombre en singular Con la primera letra en Mayuscula
- La clase debe extender otra clase "BaseCrud"
- las "columnas" deben ser en minusculas y se usa el "underscore" para representar espacios
- Los Id autincrementales deben contener el formato "id_{nombre singular tabla}" para ser mas redundantes
*como ejemplo se toma la tabla "cargos"*
- El archivo debe ser guardado con el nombre de la clase en minuscula con el underscore y la palabra modelo ej: "cargo_modelo.py"
```python
class Cargo(BaseCrud,db.Model):
    __tablename__ = 'cargos'
    id_cargo = Column(Integer, primary_key=True, autoincrement=True)
    cargo = Column(String(255), nullable=False)
```
*Se sugiere usar como plantilla el archivo "cargo_modelo.py" en caso de agregar mas tablas o abstracciones al proyecto
### 2.1.2 Preparación para la Migración de la Base de Datos

En esta sección, exploraremos los pasos necesarios para preparar una migración en nuestra aplicación. Una migración es un proceso importante en el desarrollo de aplicaciones web que implica la actualización o modificación de la estructura de la base de datos. A lo largo de esta lección, aprenderás cómo planificar y ejecutar una migración de forma efectiva, asegurando que tu base de datos esté alineada con los cambios en tu aplicación.

```bash
flask --app servidor.py db init
flask --app servidor.py db migrate -m "crear tablas iniciales" 
flask --app servidor.py db upgrade 
```

## 2.2 tutoriales que se siguieron
- https://j2logo.com/python/tutorial/
- https://j2logo.com/python/tutorial/tipo-tuple-python/
- https://pythonbasics.org/flask-boilerplate/
- https://github.com/salimane/flask-mvc
- https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
- https://flask-wtf.readthedocs.io/en/1.2.x/
- https://bulma.io/documentation/form/general/
- https://docs.reportlab.com/reportlab/userguide/ch1_intro/
- https://docs.reportlab.com/reportlab/userguide/ch7_tables/
# 3 Estructura del proyecto
En este apartado se describe la estructura del proyecto siguiendo el patrón MVC (Modelo-Vista-Controlador), con el objetivo de adherirse a las mejores **prácticas** y recomendaciones de diseño. 
## 3.1 Carpetas y archivos
En esta sección se detalla la estructura de carpetas y archivos del proyecto.
### 3.1.1 */servidor.py*
Este archivo actúa como el punto de entrada del proyecto. Es donde se inicia el servidor en un puerto específico y se añaden los controladores de archivos. Además, aquí se define la ruta de la base de datos. Este archivo también se utiliza para [*migraciones*](#2-1)

### 3.1.2 */static*
Esta carpeta contiene todos los elementos estaticos usados para la plantilla generalmente, como los CSS en este caso se uso el CSS de BULMACSS para los estilos del proyecto
### 3.1.2 */instance*
Esta carpeta se genero automaticamente al hacer la migracion y en el cual creo el archivo de SQLITE
*Si es borrado solo basta volverlo a ejecutar la "migracion" para que se restablesca la estructura y el funcionamiento*
### 3.1.4 */aplicacion*
Esta carpeta contiene subcarpetas para los controladores modelos vistas y archivos auxiliares

### 3.1.5 */aplicacion/formularios.py*
Este archivo contiene las definiciones de todos los formularios que serán utilizados por la vista. Además, se encarga de agregar las validaciones necesarias. La estructura de este archivo debe seguir las convenciones de *Flask-WTF*.
*Se recomienda agregar un formulario para cada operación CRUD correspondiente, manteniendo el nombre del modelo seguido de la palabra "Form". Por ejemplo, "CargoForm" para el modelo "Cargo".*
### 3.1.6 */aplicacion/modelos*
Esta carpeta alberga todas las abstracciones de la base de datos. Cada archivo dentro de esta carpeta debe seguir los principios de **normalización** de la estructura de la base de datos y las abstracciones, como se describe en la sección [**normalización**](#211-normalizacion-de-la-estructura-de-la-base-de-datos-y-las-abstracciones).
### 3.1.7 */aplicacion/vistas*
Esta carpeta contiene todas las vistas y fragmentos del proyecto. Se utiliza una estructura base llamada *layout*, la cual actúa como el esqueleto base para todas las páginas del proyecto.

Se siguen las siguientes reglas de normalización:

- Los CRUD deben estar en carpetas separadas, dentro de las cuales se encuentran los archivos HTML con el estilo de plantilla de Flask [Flask Template](https://flask.palletsprojects.com/en/3.0.x/tutorial/templates/).
- Los nombres de las carpetas deben estar en minúsculas y ser claros.
- Los nombres de los archivos deben estar separados por guiones bajos (_).
- Se debe evitar en la medida de lo posible la lógica condicional (IF, ELSE) en los archivos HTML para mantener un código limpio.
### 3.1.8 */aplicacion/controladores*

Esta carpeta contiene todos los controladores, y cada controlador debe seguir estas pautas:

- El nombre del controlador debe estar en singular, seguido de un guion bajo (_) y la palabra "controller". Por ejemplo: **cargo_controller**.
- Se recomienda utilizar como referencia el archivo **ejemplo_controller.py**.
- Cada controlador debe tener una variable llamada "enrutador" para mantener coherencia con la estructura del proyecto.
- Dentro de cada controlador, se utiliza (*Blueprint*)[https://flask.palletsprojects.com/es/main/blueprints/] para modularizar y dividir los casos de uso.
- Al hacer llamados a vistas o modelos desde el controlador, se recomienda importar desde la carpeta raíz **aplicacion**, como se muestra en el siguiente ejemplo:
```python
from aplicacion.modelos.cargo_modelo import Cargo
```

### 3.1.9 */aplicacion/configuracion*
Inicialmente, se contempló el uso de MySQL, por lo que se planeó tener los datos de conexión dentro de esta carpeta. Sin embargo, al final no se utilizó.