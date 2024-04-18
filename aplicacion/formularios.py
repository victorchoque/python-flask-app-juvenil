from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField,IntegerField,SelectField,RadioField,SelectMultipleField,DateField, ValidationError
from wtforms.widgets import CheckboxInput, ListWidget
from wtforms.validators import DataRequired,Regexp
from aplicacion.controladores.comun import deprecated
# Campo personalizado para el género usando radiobuttons
class EstadoField(RadioField):
    def __init__(self, *args, **kwargs):
        super(EstadoField, self).__init__(*args, **kwargs)
        self.choices = [('activado', 'Activado'), ('desactivado', 'Desactivado')]
class GeneroField(RadioField):
    def __init__(self, *args, **kwargs):
        super(GeneroField, self).__init__(*args, **kwargs)
        self.choices = [('f', 'Femenino'), ('m', 'Masculino')]
####### INICIO Campos personalizado para generar los Checkbox
# es necesario para que los Checkbox Se Marquen 
@deprecated("al final no se uso por que no resulto y se opto por el parche en codigo JavaScript")
class ChoiceObj(object):
    def __init__(self, name, choices):
        # this is needed so that BaseForm.process will accept the object for the named form,
        # and eventually it will end up in SelectMultipleField.process_data and get assigned
        # to .data
        setattr(self, name, choices)
# Dado que las pruebas realizadas no han arrojado resultados satisfactorios, se decide implementar la selección de los campos mediante JavaScript durante la edición para garantizar el marcado correcto de las casillas.
def coerce_to_true(value):
    print("COERSE" )
    print(value)
    return "1"

class InteresesCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()
    def __init__(self, label='', choices=None, validators=None, **kwargs):        
        #super(InteresesCheckboxField, self).__init__(label, validators,coerce=coerce_to_true,choices=choices, **kwargs)
        super(InteresesCheckboxField, self).__init__(label, validators,choices=choices, **kwargs)
    def process_data(self, value):
        #self.coerce= coerce_to_true,
        #self.default
        #print(self.iter_choices)
        #print(value)
        if value:
            selected_options = value.split(',')
            #self.default = ["trabaja"]
            #self.data = "Trabaja"
            #self.data = value.split(',')
            self.data = selected_options
        else:
            self.data = []

    def process_formdata(self, valuelist):
        # Recordar que estamos modificando el "data" asi que debemos tambien hacer lo inverso en el prevalidador        
        self.data = ','.join(valuelist)
        
    # TODO: Esto es muy Importante debido a que convertimos el ARRAY de los checkbox en una cadena para la base de datos, para las prevalidaciones debemos hacer lo inverso
    def pre_validate(self, form):
        # Realiza validación adicional si es necesario
        #print(self.data) # usado para hacer el DEBUG de un error que llevo 8 horas en corregirlo
        for choice in self.data.split(','):
            encontrado = False
            for key, value in self.choices:
                encontrado = True
                break
            if not encontrado :
                raise ValidationError(f"{choice} no es una opción válida.")
            
@deprecated("Se ha implementado una versión mejorada en lugar de la sugerida por ChatGPT. En nuestra base de datos, los valores se almacenan como una lista separada por comas, sin embargo, en la interfaz gráfica necesitamos representarlos como un array de casillas de verificación.")
class InteresesCheckboxField2(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()
    def __init__(self, label='', validators=None, **kwargs):
        opciones_intereses = [('interes1', 'Interes 1'),
                              ('interes2', 'Interes 2'),
                              ('interes3', 'Interes 3'),
                              ('interes4', 'Interes 4'),
                              ('interes5', 'Interes 5')]
        super(InteresesCheckboxField, self).__init__(label, validators, choices=opciones_intereses, **kwargs)
####### FIN Campos personalizado para generar los Checkbox

# Los formularios que se usaran junto a sus validaciones deben ir Aqui

class CargoForm(FlaskForm):
    cargo = StringField('Cargo', validators=[DataRequired()])
    id_cargo = HiddenField('IdCargo')
class ClienteForm(FlaskForm):
    id_cliente = HiddenField('IdCliente')        
    razon_social = StringField('Razon Social', validators=[DataRequired()])
    nit_ci = StringField('Nit o Carnet de Identidad', validators=[DataRequired()])
    #estado = StringField('Estado', validators=[DataRequired()])
    #estado = EstadoField('Estado') # usamos un campo personalizado
    estado = SelectField('Estado', validators=[DataRequired()], choices=[("activado","Activado"),("desactivado","DesActivado")] )

class EmpleadoForm(FlaskForm):
    id_cargo = SelectField('Cargo', coerce=int, validators=[DataRequired()])
    #ci = StringField('Carnet Identidad', validators=[DataRequired()])
    ci = StringField('Carnet Identidad', validators=[
        DataRequired(),
        Regexp('^[0-9]+$', message="El Carnet de Identidad debe contener solo números.")
    ])
    nombre = StringField('Nombre', validators=[DataRequired()])
    paterno = StringField('Apellido Paterno', validators=[DataRequired()])
    materno = StringField('Apellido Materno', validators=[DataRequired()])
    direccion = StringField('Dirección', validators=[DataRequired()])
    telefono = IntegerField('Teléfono', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()])
    genero = GeneroField('Género') # usamos un campo personalizado
    
    intereses = InteresesCheckboxField('Intereses',
                                       choices=[('Estudia', 'Estudia'), ('Deporte', 'Deporte'), ('Trabaja', 'Trabaja')]                                       
                                       ) # Este campo es personalizado y mas complejo
