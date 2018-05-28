import sqlite3
import random

def checkPregunta(grade, course):
	conn = sqlite3.connect('preguntas.db')
	c = conn.cursor()
	num = random.randint(1,151)
	c.execute("SELECT pregunta FROM preguntas WHERE grado=:grd AND materia=:subject AND id_pregunta=:id" , {'grd' : grade, 'subject' : course, 'id' : num})
	pregunta = c.fetchall()
	c.close()
	return pregunta

def getPregunta(grade, course):
	pregunta = checkPregunta(grade,course)
	if pregunta:
		return pregunta
	else:
		getPregunta(grade, course)
#def a(grade, materia, pregunta):
#'''
conn = sqlite3.connect('preguntas.db')
c = conn.cursor()
#c.execute("INSERT INTO preguntas VALUES (:id, :grd, :mat, :preg)", {'id' : 0, 'grd' : 0, 'mat' : 'math', 'preg' : 'Que es 1 + 1? '})
#c.close()
#'''
#a(0, 'math', 'Que es 1 + 1? ')
'''
conn = sqlite3.connect('preguntas.db')
c = conn.cursor()
c.execute("SELECT * FROM preguntas")
print(c.fetchall())
conn.close()
'''