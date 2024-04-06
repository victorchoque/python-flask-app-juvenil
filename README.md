~~Para esta documnentacion se recomienda tener un minimo de conocimiento con respecto a los archivos MD o Markdown para la jerarquia sea clara~~~(Mejorado con GPT)

Para esta documentación, se recomienda tener un mínimo de conocimiento sobre archivos MD o Markdown para garantizar que la jerarquía sea clara y se pueda aprovechar al máximo la estructura y formato proporcionados por este tipo de documentos.
# 1 python-flask-app-juvenil

## 1.1 Hacer correr el proyecto
escribir el comando
```bash
python app.py
```
## 1.2 Componentes/Librerias python a usar
- **Flask**: Flask es un framework de desarrollo web en Python que facilita la creación de aplicaciones web de forma rápida y sencilla. Es conocido por ser ligero y flexible, permitiendo a los desarrolladores construir aplicaciones web desde simples páginas estáticas hasta aplicaciones complejas con API RESTful.

- **Flask.Blueprint**: Flask.Blueprint es una característica de Flask que permite organizar y estructurar una aplicación web en módulos reutilizables y escalables. Los blueprints son útiles para dividir una aplicación en componentes más pequeños y manejables, lo que facilita el mantenimiento y la colaboración en proyectos grandes.
- 

## 1.3 Metodologia KANBAN para desarrollo este proyecto
### 1.3.1 Descripcion
Implementamos la metodología KANBAN para el desarrollo de este proyecto, el cual es de pequeña escala y tiene como objetivo servir como una demostración. En el equipo participan 4 personas, incluyendo un freelancer y tres pasantes. KANBAN nos permite gestionar las tareas de forma eficiente, visualizando el flujo de trabajo y priorizando las actividades según las necesidades del proyecto. Esta metodología nos ayuda a mantenernos organizados, colaborar de manera efectiva y realizar un seguimiento claro del progreso en todas las etapas del desarrollo


## 1.4 Herramientas externas usadas
- **ChatGPT**: Utilizamos ChatGPT para resolver dudas puntuales sobre funciones y ejemplos de programación.
- **Copilot**: Empleamos Copilot para agilizar el autocompletado de funciones rutinarias. Se recomienda su uso solo para aquellos con un nivel medio-avanzado en programación, capaces de distinguir versiones y estructuras.
- **VSCode**: Utilizamos Visual Studio Code como nuestro editor principal, que además es gratuito.
- **Git**: Utilizamos Git como sistema de gestión de versiones para controlar el desarrollo del proyecto y colaborar de manera eficiente.
- **GitHub**: Utilizamos GitHub, que nos brinda la posibilidad de utilizar Kanban para organizar y gestionar nuestras tareas de manera efectiva.


# 2 Instalar python con Flask , Flask-SQLAlchemy y Flask-Migrate
- Debes de tener instalado Python 3
- ejecutar comando "pip install Flask Flask-SQLAlchemy Flask-Migrate"
## 2.1 Migraciones?
En este apartado, se abstraen las tablas necesarias y se normalizan los nombres de los campos para facilitar su uso en una base de datos MySQL, PostgreSQL o SQLite. Una vez hecho esto, se procede a migrar dicha abstracción al gestor de base de datos elegido.

### 2.1.1 Preparar la migracion
```bash
flask --app servidor.py db init
flask --app servidor.py db migrate -m "crear tablas iniciales" 
flask --app servidor.py db upgrade 
```

## 2.2 tutorial

https://pythonbasics.org/flask-boilerplate/
https://github.com/salimane/flask-mvc
https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
# 3 Flask
## 3.1 componentes a usar en flas