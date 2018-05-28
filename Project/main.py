from flask import Flask, flash
from flask import render_template
from flask import request, g
from forms import loginForm
from flask import redirect, url_for
from forms import homeForm
from forms import juegoForm
from forms import loginAdminForm
from forms import registrarJugadorForm
from forms import adminForm
from forms import *
#from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
#from preguntas import preguntas
#from functools import wraps
#import hmac
#from hashlib import sha512
#from werkzeug.local import LocalProxy
#from werkzeug.security import safe_str_cmp
#from werkzeug.urls import url_decode, url_encode
#from flask import session, _request_ctx_stack, current_app, has_request_context
import sqlite3
#import sys
import re
#from ._compat import text_type, urlparse, urlunparse
#from .config import COOKIE_NAME, EXEMPT_METHODS
#from .signals import user_logged_in, user_logged_out, user_login_confirmed
#current_user = LocalProxy(lambda: _get_user())
userNow = ""
juego = "Mereces Tu Diploma?"
app = Flask(__name__)

#login_manager = LoginManager()
#login_manager.init_app(app)
#app.app.context()

from admin import *
from usuarios import *

def getUser():
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("SELECT * FROM current_usuario")
	user = c.fetchall()
	conn.close()
	return user

'''
def encode_cookie(payload):
	"""encode unicode to cookie, payload es el cookie y el tipo es unicode"""
	return u'{0}|{1}'.format(payload, _cookie_digest(payload))

def decode_cookie(cookie):
	"""Decodes a cookie given by encode_cookie, si verificación del cookie falla, None es retornado
		param: encoded cookie
		tipo: str
	"""
	try:
		payload, digest = cookie.rsplit(u'|', 1)
		if hasattr(digest, 'decode'):
			digest = digest.decode('ascii')
	except ValueError:
		return
	if safe_str_cmp(_cookie_digest(payload), digest):
		return payload
'''

@app.route('/', methods = ['GET', 'POST'])
def index():
	home = homeForm()
	if request.method == 'POST' and home.validate():
		if request.form.get('adminLogin', None) == 'Login para admins':
			if getUser():
				if verificarCorreoUsuario(userNow):
					return redirect(url_for('juego'))
				else:
					return redirect(url_for('admin'))
			else:
				return redirect(url_for('loginAdmin'))
		elif request.form.get('usuarioLogin', None) == 'Login para usuarios':
			if getUser():
				if verificarCorreoUsuario(userNow):
					return redirect(url_for('juego'))
				else:
					return redirect(url_for('admin'))
			else:		
				return redirect(url_for('loginJugador'))
	return render_template('home.html', title = "Mereces Tu Diploma?", form = home)

@app.route('/login')
@app.route('/user/login/', methods = ['GET', 'POST'])
def loginJugador():
	global userNow
	login = loginForm()
	if request.method == 'POST':
		if not getUser():
			if request.form['signIn'] == 'Sign In':
				#return redirect(url_for('juego'))
				#if request.form['correo'] == 'juan083099@hotmail.com':
				#if request.form['passwd'] == '123':
				if login.validate():
					return redirect(url_for('loginJugador'))
				else:
					correo = request.form['correo']
					password = request.form['passwd']
					if verificarUsuario(correo, password):
						userNow = correo
						signInUsuario(correo)
						return redirect(url_for('juego'))
					return redirect(url_for('loginJugador'))
		else:
			if verificarCorreoUsuario(userNow):
				return redirect(url_for('juego'))
			else:
				return redirect(url_for('admin'))
	return render_template('loginUsuario.html', title = "Mereces Tu Diploma? Login", form = login)

@app.route('/error/')
def error():
	return render_template('errorModal.html', title = "Errores")

@app.route('/juego')
#def login_required(f):
#	wraps(f)
def juego():
#	if g.user is None:
	'''
	if not getUser():
		return redirect(url_for('loginJugador', next = request.url))
	else:
		if not verificarCorreoUsuario(userNow):
			return redirect(url_for('admin'))
	'''
	return render_template('juego.html', title = juego)
#	return juego()

@app.route('/admin/login/', methods = ['GET', 'POST'])
def loginAdmin():
	global userNow
	if not getUser():
		login = loginAdminForm()
		if request.method == 'POST':
			if request.form['signIn'] == 'Sign In':
				#print('Error ' + str(login.validate()))
				if login.validate():
					return redirect(url_for('loginAdmin'))
				else:
					correo = request.form['correo']
					password = request.form['passwd']
					if verificarAdmin(correo, password):
						userNow = correo
						signInAdmin(userNow)
						return redirect(url_for('admin'))
					return redirect(url_for('loginAdmin'))
	else:
		if verificarCorreoAdmin(userNow):
			return redirect(url_for('admin'))
		else:
			return redirect(url_for('juego'))
	'''
	if login.validate_on_submit():
		login_user(email)
		flask.flash('Logged in succesfully.')
		next = flask.request.args.get('next')
		if not is_safe_url(next):
			return flask.abort(400)
	'''
	return render_template('loginAdmin.html', title = "Admin Login", form = login)

@app.route('/admin/', methods = ['GET', 'POST'])
def admin():
	admin = adminForm()
	if request.method == 'POST':
		if request.form.get('registrarJugador', None) == 'Registrar un nuevo jugador':
			if getUser():
				if not verificarCorreoUsuario(userNow):
					return redirect(url_for('registrarJugador'))
				else:
					return redirect(url_for('juego'))
			else:
				return redirect(url_for('loginAdmin'))
		elif request.form.get('registrarAdmin', None) == 'Registrar un nuevo admin':
			if getUser():
				if not verificarCorreoUsuario(userNow):
					return redirect(url_for('registrarAdmin'))
				else:
					return redirect(url_for('juego'))
			else:
				return redirect(url_for('loginAdmin'))
	return render_template('admin.html', title = "Admins", user = userNow, form = admin)

@app.route('/admin/registrarJugador/', methods = ['GET', 'POST'])
#@login_required
def registrarJugador():
	registrarJugador = registrarJugadorForm()
	if getUser():
		if not verificarCorreoUsuario(userNow):
			if request.method == 'POST':
				if request.form['crearUsuario'] == 'Crear Usuario':
					if not registrarJugador.validate():
						correo = request.form['correo']
						password = request.form['passwd']
						grado = request.form['grade']
						if not verificarCorreoUsuario(correo) and not verificarCorreoAdmin(correo):
							registrarUsuario(correo, password, grado)
							return redirect(url_for('admin'))
						else:
							return redirect(url_for('registrarJugador'))
					else:
						#flash('Ingrese un correo y contraseña de forma correcta')
						return redirect(url_for('registrarJugador'))
						#return render_template('registrarJugador.html', title = "Registrar Jugador", form = registrarJugador)
				return redirect(url_for('registrarJugador'))
				#return render_template('registrarJugador.html', title = "Registrar Jugador", form = registrarJugador)		
		else:
			return redirect(url_for('juego'))
		
	else:
		return redirect(url_for('loginAdmin'))
	return render_template('registrarJugador.html', title = "Registrar Jugador", form = registrarJugador)

@app.route('/admin/registrarAdmin/')
def registrarAdmin():
	registrarAdmin = registrarAdminForm()
	if getUser():
		if verificarCorreoAdmin(userNow):
			if request.method == 'POST':
				if request.form['crearAdmin'] == 'Crear Admin':
					if registrarAdmin.validate():
						correo = request.form['correo']
						password = request.form['passwd']
						if not verificarCorreoAdmin(correo) and not verificarCorreoUsuario(correo):
							match = re.search(r"(^[\w]+@[\w]+\.[\w]*\.*[com|org|edu](3)$")
							if match:
								registrarAdmins(correo, password)
								return redirect(url_for('admin'))
						else:
							return redirect(url_for('registrarAdmin'))
					else:
						return redirect(url_for('registrarAdmin'))
		else:
			return redirect(url_for('juego'))
	else:
		return redirect(url_for('loginAdmin'))
	return render_template('registrarAdmin.html', title = "Registrar Admin", form = registrarAdmin)

'''
@app.route('/user/<string:user>/juego/')
def juego(user):
	map = loadMap()
	print(map)
	lst_building = [2, 3, 4, 5]
	initial_position = [1,1]
	preguntas = preguntas()
	return render_template("juego.html", map = map, questions = preguntas, lst_building = lst_building, initial_position = initial_position)
'''

def loadMap(grado):
	'''
		Esta funcion carga un mapa que esta en un archivo plano
	'''
	l = []
	if grado in [0, 1, 2, 3, 4]:
		f = open('map1.txt', 'r')
	elif grado in [5, 6, 7, 8]:
		f = open('map2.txt', 'r')
	else:
		f = open('map3.txt', 'r')
	for line in f:
		line = line.replace('\n',' ')
		sub_list = line.split(',')
		l.append([int(num) for num in sub_list])
	f.close()
	return l

@app.route('/<string:user>/datosPersonales/')
def datosPersonales(user):
	pass

if __name__=='__main__':
	app.run(debug = True, use_reloader = True, port = 9229)

