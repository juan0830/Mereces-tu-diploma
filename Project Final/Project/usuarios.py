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

def getEmail(user):
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("SELECT correo FROM usuarios_login WHERE correo=:email", {'email' : user})
	email = c.fetchall()
	return email

def signInUsuario(emailUser):
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("INSERT INTO current_usuario (id_user, correo) VALUES (:id, :email)", {'id' : 0, 'email' : emailUser}) 
	conn.commit()
	conn.close()
	return None

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
def getGrade(emailUser):
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("SELECT grado FROM usuarios_datos WHERE correo=:email",{'email' : emailUser})
	grade = c.fetchall()
	if 'kinder' in grade[0]:
		grade = 0
	elif 'first' in grade[0]:
		grade = 1
	elif 'second' in grade[0]:
		grade = 2
	elif 'third' in grade[0]:
		grade = 3
	elif 'fourth' in grade[0]:
		grade = 4
	elif 'fifth' in grade[0]:
		grade = 5
	elif 'sixth' in grade[0]:
		grade = 6
	elif 'seventh' in grade[0]:
		grade = 7
	elif 'eigth' in grade[0]:
		grade = 8
	elif 'ninth' in grade[0]:
		grade = 9
	elif 'tenth' in grade[0]:
		grade = 10
	elif 'eleventh' in grade[0]:
		grade = 11
	conn.close()
	return grade

def getLives(emailUser):
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("SELECT vidas FROM usuarios_datos WHERE correo=:email",{'email' : emailUser})
	lives = c.fetchall()
	l = lives[0]
	return int(l[0])

def numQuestionsCorrect(emailUser):
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("SELECT preguntas_correctas FROM usuarios_datos WHERE correo=:email",{'email' : emailUser})
	corrAns = c.fetchall()
	num = corrAns[0]
	return int(num[0])

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

def logUserOut():
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("DELETE FROM current_usuario") 
	conn.commit()
	conn.close()
