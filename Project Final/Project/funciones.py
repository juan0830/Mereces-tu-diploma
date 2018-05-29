def getQuestion(grado):
	f = open('preguntas.txt', 'r')
	l = []
	l_preguntas = []
	for line in f:
		line = line.replace('\n',' ')
		sub_list = line.split(',')
		l.append(sub_list)
	f.close()
	for linea in l[1:]:
		print(linea[2])
		if int(linea[2]) == grado:
			l_preguntas.append(linea)
	for pregunta in l_preguntas:
		materia = pregunta[1]
		mat = {}
		mat['nombre'] =
		while materia == pregunta[1]:

			pass