import sqlite3

#conn = sqlite3.connect('preguntas.db')

#c = conn.cursor()
'''
c.execute("""CREATE TABLE preguntas(
			id_pregunta integer PRIMARY KEY,
			grado integer,
			materia text,
			pregunta text
	)""")

c.execute("""CREATE TABLE respuestas(
			id_pregunta integer PRIMARY KEY,
			op1 text,
			op2 text,
			op3 text,
			op4 text,			
			respuesta integer
	)""")
'''
#conn.commit()

#c.execute("""CREATE TABLE preguntas_correctas(
#			id_pregunta integer,
#			correo text
#	)""")

conn = sqlite3.connect('usuarios.db')
c = conn.cursor()

'''
c.execute("""CREATE TABLE usuarios_login(
			id_usuario integer PRIMARY KEY,
			correo text,
			passwd text
	)""")

conn.commit()

c.execute("""CREATE TABLE usuarios_datos(
			id_usuario integer PRIMARY KEY,
			correo text,
			grado integer,
			vidas integer,
			preguntas_correctas integer
	)""")

c.execute("""CREATE TABLE admin_login (
			id_admin integer PRIMARY KEY,
			correo text,
			passwd text
	) """)
'''
#c.execute("INSERT INTO preguntas VALUES (:id, :grd, :mat, :preg)", {'id':16, 'grd':2, 'mat':'math', 'preg':'Que es 10 - 5?'})
#conn.commit()
#c.execute("INSERT INTO respuestas VALUES (:id, :op1, :op2, :op3, :op4, :ans)", {'id':15, 'op1':'', 'op2':'tamben', 'op3':'tabien', 'op4':'tambien', 'ans':1})
#c.execute("INSERT INTO admin_login VALUES (:id, :correo, :passwd)", {'id': 1, 'correo': 'j@a.com', 'passwd': '123'})
#c.execute("""CREATE TABLE current_usuario (
#			id_user integer,
#			correo text
#	)""")
#c.execute("DELETE FROM current_usuario")
#c.execute("DROP TABLE preguntas")
#c.execute("SELECT * FROM preguntas")
#print(c.fetchall())
#c.execute("SELECT correo FROM current_usuario")
#c.execute("SELECT * FROM respuestas")
c.execute("SELECT * FROM admin_login")
print(c.fetchall())
#a = c.fetchall()
#b = a[0]
#print(b[0])

conn.commit()

conn.close()