from wtforms import Form
from wtforms import TextField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms import IntegerField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length, NumberRange
from wtforms.fields.html5 import EmailField
from meta import Meta

class loginForm(Form):
	"""El form para el login de los usuarios"""
	Meta()
	correo = EmailField('Correo de usuario', [Email("Ingrese un correo."),DataRequired("No deje el espacio vacío.")])
	passwd = PasswordField('Ingrese contraseña', [Length(2, 25, "La contraseña es entre 4 y 25 caracteres."),DataRequired("No deje el espacio vacío")])
	signIn = SubmitField('Sign In')

class loginAdminForm(Form):
	"""El form para el login de los admins"""
	Meta()
	correo = EmailField('Correo de usuario', [Email("Ingrese un correo."),DataRequired("No deje el espacio vacío.")])
	passwd = PasswordField('Ingrese contraseña', [Length(2, 25, "La contraseña es entre 2 y 25 caracteres."),DataRequired("No deje el espacio vacío")])
	signIn = SubmitField('Sign In')

class adminForm(Form):
	Meta()
	registrarJugador = SubmitField('Registrar un nuevo jugador')
	registrarAdmin = SubmitField('Registrar un nuevo admin')

class registrarJugadorForm(Form):
	Meta()
	"""docstring for registrarJugador"""
	correo = EmailField('Correo de usuario para registrar', [Email("Ingrese un correo."),DataRequired("No deje el espacio vacío.")])
	passwd = PasswordField('Ingrese contraseña para nuevo usuario', [Length(2, 25, "La contraseña debe ser entre 4 y 25 caracteres."),DataRequired("No deje el espacio vacío")])
	grade = SelectMultipleField('Grado', choices=[('kinder', 'kinder'),('first', 'primero'),('second', 'segundo'),('third', 'tercero'),('fourth', 'cuarto'),('fifth', 'quinto'),('sixth', 'sexto'),('seventh', 'septimo'),('eigth', 'octavo'),('ninth', 'noveno'), ('tenth', 'decimo'),('eleventh', 'once')], default = 'kinder')
	crearUsuario = SubmitField('Crear Usuario')	

class registrarAdminForm(Form):
	Meta()
	correo = EmailField('Correo de nuevo admin', [Email("Ingrese un correo."),DataRequired("No deje el espacio vacío.")])
	passwd = PasswordField('Ingrese contraseña para nuevo admin', [Length(2, 25, "La contraseña debe ser entre 4 y 25 caracteres."),DataRequired("No deje el espacio vacío")])
	crearAdmin = SubmitField('Crear Admin')	
		
class homeForm(Form):
	"""docstring for homeForm"""
	Meta()
	usuarioLogin = SubmitField('Login para usuarios')
	adminLogin = SubmitField('Login para admins')

class juegoForm(Form):
	"""docstring for juegoForm"""
	Meta()
	pass
		


