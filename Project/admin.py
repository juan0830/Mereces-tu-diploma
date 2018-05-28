import sqlite3
#from main import login_manager

#class Admin():
"""docstring for Admin"""
'''
conn = sqlite3.connect('usuarios.db')
c = conn.cursor()
c.execute("SELECT id_admin FROM admin_login")
idAdmin = c.fetchall()
c.execute("SELECT correo FROM admin_login")
email = c.fetchall()
c.execute("SELECT passwd FROM admin_login")
passwd = c.fetchall()
conn.close()
'''
	
def verificarAdmin(correo, passwd):
	email = getEmail(correo)
	if email:
		password = checkPassword(correo, passwd)
		if password:
			return True
	return False

def verificarCorreoAdmin(correo):
	email = getEmail(correo)
	if email:
		return True
	else:
		return False

def signInAdmin(emailUser):
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("INSERT INTO current_usuario (id_user, correo) VALUES (:id, :email)", {'id' : 0, 'email' : emailUser})
	#c.execute("UPDATE current_usuario SET correo = :email WHERE id_user = 0", {'email' : emailUser})
	conn.commit()
	conn.close()

def registrarAdmins(emailAdmin, password):
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("INSERT INTO admin_login (correo, passwd) VALUES (:email, :pw)", {'email' : emailAdmin, 'pw' : password})
	conn.commit()
	conn.close()

#def load_user(admin_id):
#	conn = sqlite3.connect('usuarios.db')
#	c = conn.cursor()
#	c.execute("SELECT * FROM admin_login WHERE id_admin =:id", {'id': admin_id})
#	return c.fetchall()

def getEmail(emailUser):
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("SELECT correo FROM admin_login WHERE correo=:email", {'email' : emailUser})
	email = c.fetchall()
	conn.close()
	return email

def checkPassword(emailUser, password):
	conn = sqlite3.connect('usuarios.db')
	c = conn.cursor()
	c.execute("SELECT passwd FROM admin_login WHERE correo=:email AND passwd=:pw", {'email': emailUser, 'pw' : password})
	password = c.fetchall()
	conn.close()
	return password
'''
@login_manager.user_loader
def load_user(user_id):
	return User.get(user_id)

def is_authenticated(self):
	return True

def is_active(self):
	return True

def is_anonymous(self):
	return False

def get_id(self):
	return unicode(self.id)
'''
'''
conn = sqlite3.connect('usuarios.db')
c = conn.cursor()
c.execute("SELECT * FROM admin_login")
print(c.fetchall())
#c.execute("DELETE FROM current_usuario")
#conn.commit()
conn.close()
'''

#signInAdmin('juan083099@hotmail.com')
#print(verificarAdmin('juan083099@hotmail.com', 'JUKASWE'))
