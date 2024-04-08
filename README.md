~~Para esta documnentacion se recomienda tener un minimo de conocimiento con respecto a los archivos MD o Markdown para la jerarquia sea clara~~(Mejorado con GPT)

Para esta documentación, se recomienda tener un mínimo de conocimiento sobre archivos MD o Markdown para garantizar que la jerarquía sea clara y se pueda aprovechar al máximo la estructura y formato proporcionados por este tipo de documentos.
# 1 python-flask-app-juvenil

## 1.1 Para Hacer Ejecutar el proyecto
escribir el comando
```bash
python servidor.py
```
## 1.2 Componentes/Librerias python a usar
- **Flask**: Flask es un framework de desarrollo web en Python que facilita la creación de aplicaciones web de forma rápida y sencilla. Es conocido por ser ligero y flexible, permitiendo a los desarrolladores construir aplicaciones web desde simples páginas estáticas hasta aplicaciones complejas con API RESTful.

- **Flask.Blueprint**: Flask.Blueprint es una característica de Flask que permite organizar y estructurar una aplicación web en módulos reutilizables y escalables. Los blueprints son útiles para dividir una aplicación en componentes más pequeños y manejables, lo que facilita el mantenimiento y la colaboración en proyectos grandes.

- **Flask-SQLAlchemy**:Flask-SQLAlchemy es una extensión de Flask que proporciona una integración sencilla entre Flask y SQLAlchemy, un popular ORM (Mapeo Objeto-Relacional) para Python. Flask-SQLAlchemy simplifica la configuración y el uso de SQLAlchemy en aplicaciones Flask, permitiendo a los desarrolladores trabajar con bases de datos de manera más eficiente y fácilmente.

- **Flask.Migrate**: Flask-Migrate es una extensión de Flask que proporciona herramientas para gestionar y realizar migraciones de base de datos de manera sencilla y segura. Las migraciones de base de datos son cambios en la estructura de la base de datos que deben aplicarse de manera coherente a lo largo del tiempo, y Flask-Migrate simplifica este proceso al automatizar la generación y aplicación de scripts de migración.

- **Flask-WTF**:Flask-WTF es una extensión de Flask que proporciona integración con la biblioteca WTForms, que facilita la creación y validación de formularios en aplicaciones web Flask. Flask-WTF simplifica la creación de formularios HTML y el manejo de datos de formulario en las vistas de Flask, ayudando a los desarrolladores a construir formularios seguros y fáciles de usar con facilidad.

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

# 2 Instalar python con Flask , Flask-SQLAlchemy , Flask-Migrate y Flask-WTF
- Debes de tener instalado Python 3 (por DEFAULT instala el comando "PIP")
- ejecutar comando "pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-WTF "
```bash
cd c:\proyectos\RutaDeEstaCarpeta\
pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-WTF
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

# 3 Estructura del proyecto
para lo siguiente se la estructura MVC, tratando de seguir las recomendaciones 
## 3.1 Carpetas y archivos
### 3.1.1 */servidor.py*
Este es el punto de entrada del proyecto donde se inicia por el puerto y donde se agrega los archivos controladores ,se define la ruta de la base de datos y tambien es el archivos usado para las [*migraciones*](#2-1)
### 3.1.2 */static*
Esta carpeta contiene todos los elementos estaticos usados para la plantilla generalmente, como los CSS en este caso se uso el CSS de BULMACSS para los estilos del proyecto
### 3.1.2 */instance*
Esta carpeta se genero automaticamente al hacer la migracion y en el cual creo el archivo de SQLITE
*Si es borrado solo basta volverlo a ejecutar la "migracion" para que se restablesca la estructura y el funcionamiento*
### 3.1.4 */aplicacion*
Esta carpeta contiene subcarpetas para los controladores modelos vistas y archivos auxiliares

### 3.1.5 */aplicacion/formularios.py*
es un archivo que contiene las definiciones de todos los formularios que usara la vista tambien sirve para agregar las validaciones se debe de estructurar segun *Flask-WTF*
*Se recomienda agregar el formulario para el CRUD correspondiente, manteniendo el nombre del Modelo Seguido de la palabra form como "CargoForm"*

### 3.1.6 */aplicacion/modelos*
esta carpeta contiene todas las abastracciones de la base de datos donde cada archivo debe estar [**normalizado**](#211-normalizacion-de-la-estructura-de-la-base-de-datos-y-las-abstracciones)

### 3.1.7 */aplicacion/vistas*
esta carpeta contiene todas las vistas fragmentos , para este proyecto se usa una estrcutura base llamada *layout* el cual servira como esqueleto base para todas las paginas
Se normaliza las siguientes reglas
- Los CRUD deben ir en carpetas y dentro de las carpetas deben estar los archivos HTML el estilo de plantilla de flask [Flask Template](https://flask.palletsprojects.com/en/3.0.x/tutorial/templates/)
- las carpetas deben estar con el nombre claro en minusculas
- los archivos deben ir separados por el underscore(_)  
- no debe  contener mucha logica IF,ELSE tratar de evitarlo lo mayor posible para tener un codigo limpio
### 3.1.8 */aplicacion/controladores*
esta carpeta contiene todos los controladores y se cada controlador debe cumplir lo siguiente
- Nombre del controlador en singular seguido del underscore(_) y de la palabra "controller" ejemplo: **cargo_controller**
- Tomar como ejemplo el archivo **ejemplo_controller.py**
- El controlador debe tener la variable "enrutador" para mantener una coherencia con toda la estructura del proyecto
- Dentro de cada controlador se hace uso de (*Blueprint*)[https://flask.palletsprojects.com/es/main/blueprints/] para mantener esa modularizacion y tratar de dividir los casos de uso
- Con el controlador se hace llamados a las vistas u modelos, se recomienda hacer los llamados desde la carpeta raiz **aplicacion** cada que es use un import/from como ejm: 
```python
from aplicacion.modelos.cargo_modelo import Cargo
```

### 3.1.9 */aplicacion/configuracion*
Se penso hacer uso de MYSQL por lo cual se penso en tener los datos de conexion dentro de esta carpeta, pero al final no se uso