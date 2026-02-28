from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, Label
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('id',[
                            validators.DataRequired(message="El campo es requerido"),
                            validators.NumberRange(min=2,max=100, message="Ingresa un valor valido")])
    nombre = StringField('nombre',[
                            validators.DataRequired(message="El campo es requerido"),
                            validators.Length(min=4,max=10, message="Ingresa un valor valido")])    
    apellidos = StringField('apellidos',[
                            validators.DataRequired(message="El campo es requerido"),
                            validators.Length(min=2,max=100, message="Ingresa un valor valido")])
    email = EmailField('email',[
                            validators.Email(message="Ingrese un email valido")])

    telefono = IntegerField('telefono',[
                            validators.NumberRange(min=10,max=13, message="Ingresa un Número de Teléfono valido")])
