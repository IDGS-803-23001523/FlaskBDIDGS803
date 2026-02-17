from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id=IntegerField('id')
    nombre=StringField('Nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4,max=20, message='Requiere min=4 max=20')
    ])
    apaterno=StringField('Apaterno', [
        validators.DataRequired(message='El apellido es requerido')
    ])
    email=EmailField('Correo', [
        validators.DataRequired(message='El email es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
