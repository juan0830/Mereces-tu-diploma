import sqlite3
#from main import login_manager

def verificarUsuario(correo, passwd):
	email = getEmail(correo)
	if email:
		password = checkPassword(correo, passwd)
		if password:
			return True
	return False

def verificarCorreoUsuario(correo):
	email = getEmail(correo)
	if email:
		return True
	else:
		return False

def signInUsuario(emailUser):
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("INSERT INTO current_usuario (id_user) SELECT id_usuario FROM usuarios_login WHERE correo=:email", {'email' : emailUser}) 
	c.execute("UPDATE current_usuario SET correo = :email WHERE id_user = 0", {'email' : emailUser})
	conn.commit()
	conn.close()
	pass

def registrarUsuario(emailUser, password, grade):
	lives = 3
	answers = 0
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("INSERT INTO usuarios_login (correo, passwd) VALUES (:email, :pw)", {'email' : emailUser, 'pw' : password})
	c.execute("""INSERT INTO usuarios_datos (correo, grado, vidas, preguntas_correctas) 
					VALUES (:email, :grade, :lives, :ans)""", {'email' : emailUser, 'grade' : grade, 'lives' : lives, 'ans' : answers})
	conn.commit()
	conn.close()
	pass
#def load_user(usuario_id):
#	conn = sqlite3.connect('usuarios.db')
#	c = conn.cursor()
#	c.execute("SELECT * FROM usuario_login WHERE id_usuario =:id", {'id': usuario_id})
#	return c.fetchall()

def getEmail(emailUser):
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("SELECT correo FROM usuarios_login WHERE correo=:email", {'email' : emailUser})
	email = c.fetchall()
	conn.close()
	return email

def checkPassword(emailUser, password):
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("SELECT passwd FROM usuarios_login WHERE correo=:email AND passwd=:pw", {'email': emailUser, 'pw' : password})
	password = c.fetchall()
	conn.close()
	return password